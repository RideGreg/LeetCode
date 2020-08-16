# Q: 找很大的文件中出现次数top 10的单词


# A: 大文件意味着不能在内存同时存下所有的key 也就不可以维持一个全局counter。
# 必须先大文件按key分割 （hash或者排序），然后对每一个小文件算top10再合并结果。类似于MapReduce

# https://www.pdai.tech/md/algorithm/alg-domain-bigdata-devide-and-hash.html
# 大数据处理思路: 分而治之/Hash映射 + Hash_map统计 + 堆/快速/归并排序
# 说白了，就是先映射，而后统计，最后排序:

# 1 分而治之/hash映射: 针对数据太大，内存受限，只能是: 把大文件化成(取模映射)小文件。 E.g.
# 依次从大文件读入key，取hash(x)%1000，按该值写入1000个小文件
# 2 hash_map统计: 对每个小文件，采用Trie或常规的hash_map(word，value)来统计每个文件中出现的词以及相应的频率。 
# 3 堆/快速排序: 统计完了之后，在每个小文件自身进行排序(可采取堆排序)，得到次数最多的words。
# 最好把1000个小文件的top k进行归并排序。
