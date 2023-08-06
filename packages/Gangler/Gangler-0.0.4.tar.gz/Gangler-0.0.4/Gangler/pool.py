# to compare date with mutiple aim
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Gangler import prepare
from matplotlib import pyplot


def initiation(a):
    gene = a.result['gene'].tolist()
    variation_num = a.result['variation_number'].tolist()
    # normalization
    # n = a.result[a.result['gene'] == 'ttn-1']['variation_number'].tolist()[0]
    n = sum(variation_num)
    variation_num = [a*100 / n for a in variation_num]
    pool_file = pd.DataFrame({'gene': gene, 'variation_number': variation_num})
    return pool_file


class snpool:
    def __init__(self, readfile_list, target_list):
        self.target = target_list
        self.initiation_list = []
        self.result = []
        self.readfile_list = readfile_list
        self.variation_list = pd.DataFrame()
        self.get_start()

    def get_start(self):
        genelist = []
        for i in self.readfile_list:
            filter(i, 3, rid=[])
            genelist.extend(i.result['gene'].to_list())
        genelist = list(set(genelist))
        for i in self.readfile_list:
            local_gene = i.result['gene'].to_list()
            local_variation = i.result['variation_number'].to_list()
            for j in genelist:
                if not j in local_gene:
                    local_gene.append(j)
                    local_variation.append(int(0))

            final_variation = [n+0.1 for n in local_variation]
            sum_var = sum(final_variation)
            fin_var = [n*100/sum_var for n in final_variation]
            self.initiation_list.append(pd.DataFrame({"gene":local_gene,"variation_number":fin_var}))
        array = []
        var_list = []
        for i in genelist:
            target = []
            for j in self.initiation_list:
                m = j[j['gene'] == i]['variation_number'].tolist()
                target.extend(m)
            var_list.append(target)
            target = percentage(target)
            array.append(target)
        np.asarray(array)
        col = self.target
        self.result = pd.DataFrame(array, columns=col)
        self.result.insert(loc=0, column='gene', value=genelist)
        self.variation_list = pd.DataFrame(var_list,columns=col)
        self.variation_list.insert(loc=0, column='gene', value=genelist)
    def plot(self,gene):
        x = self.target
        y = list(self.variation_list.loc[self.variation_list['gene'] == gene].values)[0][1:]
        plt.scatter(x,y)


# def sigma(list_ele):
#     max_val = max(list_ele)
#     mean_l = []
#     for i in list_ele:
#       mean_l.append(i)
#     mean_l.remove(max_val)
#     sqr = np.var(mean_l)
#     mean = np.mean(mean_l)
#     dist = (max_val - mean)**2
#     j = sqr/dist
#     m_list = ['_'] * len(list_ele)
#     if j != 'NA':
#         for i in range(len(list_ele)):
#             if list_ele[i] == max(list_ele):
#                 m_list[i] = j
#     return m_list


# pick gene and variation_number

def percentage(list_ele):
    total = 0
    iter_num = len(list_ele)
    new_list = []
    j = 1
    for i in range(iter_num):
        total = total + list_ele[i]
    for i in range(iter_num):
        if total != 0:
            m = list_ele[i] / total
        else:
            m = 1
        j = j * m
        new_list.append(m)
    if max(list_ele) != min(list_ele):
        j = (j / (max(new_list) * (max(list_ele) - min(list_ele)) ** len(list_ele)))**(1/len(list_ele))
    else:
        j = 'NA'
    m_list = ['_']*len(new_list)
    if j != 'NA':
      for i in range(len(new_list)):
        if new_list[i] == max(new_list):
            m_list[i] = j/new_list[i]
    return m_list


def find(a):
    #  合并df
    prepare.get_impact(a)
    a.candidate = []
    a.suppressor_group = []
    co_data = pd.DataFrame()
    for i in range(len(a.taglist)):
        co_data = pd.concat([co_data, a.taglist[i]])
        a.co_data = co_data
    a.result = get(co_data)
    print(a.result)
    return get(co_data)


# get为核心分析函数
def get(co_data):
    co_data.drop_duplicates()
    result = []
    index = list(set(list(co_data['gene'])))
    for i in range(len(index)):
        res = []
        ind = search(co_data, 'gene', index[i])
        co = pd.DataFrame(co_data.loc[ind, :])
        mut_ind = []
        var_ind = []
        var_fin = []
        var = []
        name = []
        for k, v in co.iterrows():
            name = v['gene']
            mut_ind.append(v['tag'])
            var_ind.append(v['protein'])
            var = list(set(var_ind))

        for q in range(len(var)):
            var_count_ind = search(co, 'protein', var[q])
            var_count = pd.DataFrame(co.loc[var_count_ind, :]).shape[0]
            var_fin.append([var[q], var_count])
        res.append([list(set(mut_ind)), len(set(mut_ind)), name, var_fin, len(var_fin)])
        result.extend(res)
    result = pd.DataFrame(result, columns=['sample', 'size', 'gene', 'variation', 'variation_number'])
    result = result[~result['variation'].isin([[]])]
    result = result.sort_values(by=['size'], ascending=False)
    result = result.reset_index(drop=True)
    return result


def filter(a, lengthlimit=4, rid=[]):
    prepare.get_impact(a)
    a.candidate = []
    a.suppressor_group = []
    conc = pd.DataFrame()
    for i in range(len(a.taglist)):
        conc = pd.concat([conc, a.taglist[i]])
    filter = conc.groupby(['gene', 'protein', 'ID', 'base']).filter(lambda x: len(x) <= lengthlimit)
    a.co_data = filter
    result = get(filter)
    result = result[~result['gene'].isin(rid)]
    n = result.shape[0]
    result.index = list(range(n))
    a.result = result
    return result


def search(df, col, kw):
    return df[col] == kw
