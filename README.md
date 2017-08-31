# Docker MeCab Neologd Cabocha sklearn jupyter-notebook pandas

## setup

```
$ docker build -t mecab-jupyter ./docker
$ docker run --name mecab-jupyter -it -p 8888:8888 -v `pwd`:/mecab-jupyter mecab-jupyter:latest 
```

mount `/mecab-jupyter` to this directory

## run jupyter notebook

```
$ jupyter-notebook --ip=0.0.0.0 --NotebookApp.token= --allow-root
```

