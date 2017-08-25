# https://ja.wikipedia.org/wiki/Wikipedia:データベースダウンロード
curl -SL -o jawiki-latest-pages-articles.xml.bz2 https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
git clone https://github.com/attardi/wikiextractor
python3.6 wikiextractor/WikiExtractor.py -b 100G -o ./wikipedia_data/extracted ./wikipedia_data/jawiki-latest-pages-articles.xml.bz2
