def create_matrix(rows, cols):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    outer_list=[]
    for i in range(0,rows):
        inner_list=[]
        for j in range(i,cols+i):
            inner_list.append((alphabet[i])+alphabet[j]+alphabet[i])
            translation = {39: None} 
        outer_list.append(str(inner_list).translate(translation))
    return '{0}'.format(str(outer_list).translate(translation))
# Write a function to generate a matrix of 3 letters palindromes with x number of rows and y number of columns.
# Function should return a string representation of the matrix
# For example

# create_matrix(3, 3) --> "[[aaa, aba, aca], [bbb, bcb, bdb], [ccc, cdc, cec]]"
# "[[aaa, aba, aca, ada, aea, afa, aga, aha, aia, aja], [bbb, bcb, bdb, beb, bfb, bgb, bhb, bib, bjb, bkb], "
#         expected += "[ccc, cdc, cec, cfc, cgc, chc, cic, cjc, ckc, clc], [ddd, ded, dfd, dgd, dhd, did, djd, dkd, dld, dmd],"
#         expected += " [eee, efe, ege, ehe, eie, eje, eke, ele, eme, ene], [fff, fgf, fhf, fif, fjf, fkf, flf, fmf, fnf, fof], "
#         expected += "[ggg, ghg, gig, gjg, gkg, glg, gmg, gng, gog, gpg], [hhh, hih, hjh, hkh, hlh, hmh, hnh, hoh, hph, hqh], "
#         expected += "[iii, iji, iki, ili, imi, ini, ioi, ipi, iqi, iri], [jjj, jkj, jlj, jmj, jnj, joj, jpj, jqj, jrj, jsj]]"
#         test.assert_equals(create_matrix(10, 10), expected)
