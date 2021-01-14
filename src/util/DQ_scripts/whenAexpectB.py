def whenAexpectB(data, A, B, ColumnATerm, ColumnBTerm):   
    try:
        data=data
        a = data[A]
        b = data[B]
        c = pd.merge(a, b, left_index=True, right_index=True)
        z = c.loc[(c[A] == ColumnATerm ) & (c[B] <= ColumnBTerm)]
        return z
              
    except:
        print('Housten, We have a problem!')
        raise ValueError('Check that the columns are defined properly')
