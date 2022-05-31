:param apiKey => "AIzaSyDDHL2HxEz8toGP6ACG6R-CTpxSpXFrREY";


CREATE INDEX FOR (n:Source) ON n.source;
CREATE INDEX FOR (n:News) ON n.newsID;

:auto USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///gossipcop_fake.csv" as csv
WITH csv WHERE csv.news_url IS NOT NULL
MERGE(n:News{newsID:csv.id,title:csv.title,url:csv.news_url})
SET n.fake = 1
MERGE(ns:Source{source:split(csv.news_url,"/")[0]})
MERGE(n)-[:HAS_SOURCE]->(ns);


CALL apoc.periodic.iterate("MATCH (a:News)
WITH a  WHERE not exists((a)-[:ENTITY]->()) 
WITH a LIMIT 500
WITH collect(a) as col
UNWIND col as a RETURN a",
"CALL apoc.nlp.gcp.entities.stream(a, {
  key: $apiKey,
  nodeProperty: 'title'
})
YIELD value
UNWIND value.entities AS entity
MERGE (e:Entity {name: entity.name})
SET e.type = entity.type
MERGE (a)-[:ENTITY]->(e)",{batchsize:1000,params:{apiKey:$apiKey}});

:auto USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///gossipcop_real.csv" as csv
WITH csv WHERE csv.news_url IS NOT NULL
MERGE(n:News{newsID:csv.id,title:csv.title,url:csv.news_url})
SET n.fake = 0
MERGE(ns:Source{source:split(split(csv.news_url,"//")[1],"/")[0]})
MERGE(n)-[:HAS_SOURCE]->(ns);


:auto USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///politifact_fake.csv" as csv
WITH csv WHERE csv.news_url IS NOT NULL
MERGE(n:News{newsID:csv.id,title:csv.title,url:csv.news_url})
SET n.fake = 1
MERGE(ns:Source{source:split(csv.news_url,"/")[0]})
MERGE(n)-[:HAS_SOURCE]->(ns);

MATCH p=(n:News)-[:HAS_SOURCE]->(ns) where n.newsID contains "politi" and (ns.source="http:" or ns.source="https:") WITH n, ns 
MERGE(ns2:Source{source:split(split(n.url,"//")[1],"/")[0]}) MERGE(n)-[:HAS_SOURCE]->(ns2) 
WITH ns DETACH DELETE ns;

:auto USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///politifact_real.csv" as csv
WITH csv WHERE csv.news_url IS NOT NULL
MERGE(n:News{newsID:csv.id,title:csv.title,url:csv.news_url})
SET n.fake = 0
MERGE(ns:Source{source:split(split(csv.news_url,"//")[1],"/")[0]})
MERGE(n)-[:HAS_SOURCE]->(ns);


MATCH (a:News)
WITH a  WHERE a.newsID contains "gossip" and not exists((a)-[:ENTITY]->()) 
MERGE(e:Entity{name:"Fake"})
MERGE(a)-[:ENTITY]->(e);



Call apoc.periodic.iterate("MATCH (c1:News)-[:HAS_SOURCE|:ENTITY] ->(n)<- [:HAS_SOURCE|:ENTITY]-(c2:News)
    WHERE id(c1)<>id(c2)
    WITH distinct c1,c2, count(*) as cnt WHERE cnt>1 RETURN c1,c2,cnt","MERGE (c1) - [:SHARED {count: cnt}] -> (c2)",{batchsize:1000});


CALL gds.nodeSimilarity.mutate('news_graph',
        {
            similarityCutoff: 0.05,
            concurrency: 4,
            mutateRelationshipType:'SIMILAR_TO',
            mutateProperty:'score',
            relationshipWeightProperty:'count'
        }                   
    );
CALL gds.degree.mutate('news_graph',
{
    nodeLabels: ['News'],
    relationshipTypes:['SIMILAR_TO'],
    relationshipWeightProperty: 'score',
    mutateProperty: 'si_risk_score'
}                   
)


CALL gds.graph.writeNodeProperties(
      'news_graph',
      ['si_risk_score'],
      ['News'],
      { writeConcurrency: 4 }
    );

CALL apoc.periodic.iterate(
        "MATCH (c1:News) - [t:SHARED] -> (c2:News) RETURN c1, c2, t",
        "MERGE (c1)-[:RELATED_TO{weight:t.count+c1.si_risk_score+c2.si_risk_score}]->(c2)",
        {batchSize:1000}
    );

MATCH(a:News)-[:SHARED]->()  WHERE a.fake=0 WITH a ORDER BY rand() LIMIT 3100 SET a:ModelInput;
MATCH(a:News)-[:SHARED]->()  WHERE a.fake=1 SET a:ModelInput;


CALL gds.graph.drop('news_graph');
