def create_client(tx,parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MERGE (c:Client {id:param.id,age:param.age,full_name:param.full_name,sex:param.sex})
        ''',parameters=parameters
    )


def create_address(tx,parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MATCH (c:Client {id:param.id})
        MERGE (a:Address {address:param.address})
        MERGE (c) - [:IS_AT] -> (a)
        ''',parameters=parameters
    )

def create_marital(tx, parameters):
        '''
        You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
        :param tx:
        :param parameters:
        :return:
        '''
        tx.run(
            '''
            UNWIND $parameters as param
            MATCH (c:Client {id:param.id})
            MERGE (m:Marital {marital_status:param.marital_status})
            MERGE (c) - [:IS] -> (m)
            ''', parameters=parameters
        )



def create_account(tx, parameters):
        '''
        You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
        :param tx:
        :param parameters:
        :return:
        '''
        tx.run(
            '''
            UNWIND $parameters as param
            MATCH (c:Client {id:param.id})
            MERGE (a:Account {account_id:param.account_id,defaulter:param.default_payment_next_month,limit_balancer:param.limit_balance})
            MERGE (c) - [:HAS_A] -> (a)
            ''', parameters=parameters
        )


def create_payment1(tx, parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MATCH (a:Account {account_id:param.account_id})
        MERGE (p:Payment {paymentAmount:param.pay_amt_1})
        MERGE (a) - [:MADE_A {month:"July"}] -> (p)
        ''', parameters=parameters
    )


def create_payment2(tx, parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MATCH (a:Account {account_id:param.account_id})
        MERGE (p:Payment {paymentAmount:param.pay_amt_2})
        MERGE (a) - [:MADE_A {month:"August"}] -> (p)
        ''', parameters=parameters
    )

def create_payment3(tx, parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MATCH (a:Account {account_id:param.account_id})
        MERGE (p:Payment {paymentAmount:param.pay_amt_3})
        MERGE (a) - [:MADE_A {month:"September"}] -> (p)
        ''', parameters=parameters
    )


def create_payment4(tx, parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MATCH (a:Account {account_id:param.account_id})
        MERGE (p:Payment {paymentAmount:param.pay_amt_4})
        MERGE (a) - [:MADE_A {month:"October"}] -> (p)
        ''', parameters=parameters
    )

def create_payment5(tx, parameters):
        '''
        You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
        :param tx:
        :param parameters:
        :return:
        '''
        tx.run(
            '''
        UNWIND $parameters as param
        MATCH (a:Account {account_id:param.account_id})
        MERGE (p:Payment {paymentAmount:param.pay_amt_5})
        MERGE (a) - [:MADE_A {month:"November"}] -> (p)
            ''', parameters=parameters
        )


def create_payment6(tx, parameters):
    '''
    You want to make sure that the parameters (which will be in a datastructure) have a length that cooresponds to a reasonable batch size.
    :param tx:
    :param parameters:
    :return:
    '''
    tx.run(
        '''
        UNWIND $parameters as param
        MATCH (a:Account {account_id:param.account_id})
        MERGE (p:Payment {paymentAmount:param.pay_amt_6})
        MERGE (a) - [:MADE_A {month:"December"}] -> (p)
        ''', parameters=parameters
    )
