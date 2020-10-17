# Time:  O(|V| + |E|)
# Space: O(|V|)

# 1236
# Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links
# that are under the same hostname as startUrl.
#
# Return all urls obtained by your web crawler in any order.
#
# Your crawler should:
# - Start from the page: startUrl
# - Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
# - Do not crawl the same link twice.
# - Explore only the links that are under the same hostname as startUrl.

# In sample url http://exmaple.org:8888/foo/bar#bang, hostname is "example.org", host is "example.org:8888"
# For simplicity sake, you may assume all urls use http protocol without any port specified.
# For example, the urls http://leetcode.com/problems and http://leetcode.com/contest are under the same
# hostname, while urls http://example.org/test and http://example.com/abc are not under the same hostname.

# Constraints:
# 1 <= urls.length <= 1000, 1 <= urls[i].length <= 300
# You may assume there're no duplicates in url library.


# SOLUTION: Use DFS/BFS to search start from the startURL. Remember to get rid of duplicate URLs.

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """
       pass


class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        SCHEME = "http://"
        def hostname(url):
            pos = url.find('/', len(SCHEME))
            if pos == -1:
                return url
            return url[:pos]

        result = [startUrl]
        lookup = set(result)
        for from_url in result:
            name = hostname(from_url)
            for to_url in htmlParser.getUrls(from_url):
                if to_url not in lookup and name == hostname(to_url):
                    result.append(to_url)
                    lookup.add(to_url)
        return result

urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]

urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]