class Solution:
    def convert(self, s: str, numRows: int) -> str:
        from math import ceil

        def ins_stuff_to_lst(lst,idx,stuff_lst): 
            # to insert the elements of (stuff_lst) in the initial list (lst) in the given index (idx)
            for element in stuff_lst:
                lst. insert(idx, element)
                idx += 1
            return lst

        def lst_to_str (l2):
            string = ''.join([str(item)for item in l2])
            return string

        # modified parameters
        n =  numRows
        n_spaces = n-2      # n_spaces = n_ones  
        n_periods = n-1       
        stage_length = n + n_periods * n_spaces + n_spaces
        try:
            n_stages = ceil(len(s)/(stage_length - n_periods * n_spaces))+1
        except:
            n_stages = 1        #to avoid Zero division error
            
            
        # convert the given string to list
        s_list=[]
        s_list[:0]= str(s)


        # Adding extra spaces to the string list  (check the picture with the code)
        idx = 0
        for stage in range (n_stages):

            idx = idx + n                                            # shifting the index
            s_list =  ins_stuff_to_lst(s_list,idx, [' '] * n_spaces) # adding spaces
            idx = idx + n_spaces                                     # shifting the index

            for period in range (n_periods-1):
                idx = idx + 1
                s_list =  ins_stuff_to_lst(s_list,idx, [' '] * n_spaces)
                idx = idx + n_spaces


        # creating an array(nested list) as rows
        printing_arr = [[]*4 for _ in range(n)]

        for idx_col in range( ceil(len(s_list)/n) ):
             for idx_row in range(n):
                 try:
                     printing_arr[idx_row].append( s_list[n*idx_col+idx_row] )
                 except:
                     break

        # converting the list to a one concatenated string
        printing_string = ''
        for row in printing_arr:
            printing_string = printing_string + lst_to_str(row) 
        
        return  printing_string.replace(" ", "")

            
            
            
            
        