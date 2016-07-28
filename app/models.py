import pandas as pd
from app import engine


def search_last(last):
    sql_text = 'SELECT * FROM odyssey WHERE lastname_stripped LIKE "%' + last + '%";'
    df = pd.read_sql_query(sql_text, engine)
    
    
    
    return dfr


def search_all(first, last, case):
    if case:
        print 'Searching for case = ', case
        sql_text = 'SELECT * FROM odyssey WHERE "Case Number" LIKE "%' + case + '%";'
        df = pd.read_sql_query(sql_text, engine)
        #print 'len(df) = ', len(df)
    elif last:
        print 'Searching for last = ', last
        sql_text = 'SELECT * FROM odyssey WHERE lastname_stripped LIKE "%' + last + '%";'
        df = pd.read_sql_query(sql_text, engine)
        #print 'len(df) = ', len(df)
    elif first:
        print 'Searching for first = ', first
        #print 'Only first name entered, searching for first name= ', first
        sql_text = 'SELECT * FROM odyssey WHERE firstname_stripped LIKE "%' + first + '%";'
        df = pd.read_sql_query(sql_text, engine)
        #print 'len(df) = ', len(df)
        #print 'After first name search, df= ', df
    if len(df) > 1:
        #print 'len(df) = ', len(df)
        if first:
            print 'Searching for first after initial search. First = ', first
            df = df.loc[df['firstname_stripped'].str.contains(first)]
    if len(df) == 0:
        print "Need to add NO RESULTS prompt and return to index"
    print 'Done with search'
    
    
    df.drop(['last_name', 'firstname_stripped', 'first_name', 'lastname_stripped', 'index', 'Connection Type'], axis=1, inplace=True)
    #df.drop ?? in pandas  df.drop('name of column', axis=1 **where it is)
    
    return df


if __name__ == "__main__":

    last_name = 'AAGAARD'
    df_db_out = search_last(last_name)
    print
    print "FROM MAIN:"
    print df_db_out.to_html()
