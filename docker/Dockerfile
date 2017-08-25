FROM centos:7

ENV LANG en_US.UTF-8

ENV mecab_url   https://github.com/taku910/mecab/archive/master.tar.gz
ENV neologd_url https://github.com/neologd/mecab-ipadic-neologd/archive/master.tar.gz
ENV crfpp_url   https://github.com/taku910/crfpp/archive/master.tar.gz
ENV cabocha_url https://github.com/taku910/cabocha/archive/master.tar.gz

RUN yum -y update \
    && yum -y groupinstall "Development Tools" \
    && mkdir /tools \
    # python 3
    && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
    && yum -y install python36u python36u-pip python36u-devel \
    && cp /etc/skel/.bashrc ~/.bashrc \
    && python3.6 -m venv python3.6 \
    && source /python3.6/bin/activate \
    && echo 'source /python3.6/bin/activate' >> ~/.bashrc \
    # ld library path
    && echo '/usr/local/lib' >> /etc/ld.so.conf.d/local.conf \
    && ldconfig \
    # mecab
    && cd /tools \
    && curl -SL -o mecab-master.tar.gz ${mecab_url} \
    && tar zxf mecab-master.tar.gz \
    && cd mecab-master/mecab \
    && ./configure --enable-utf8-only --with-charset=utf8 \
    && make \
    && make install \
    && ldconfig \
    && cd ../mecab-ipadic \
    && ./configure --with-charset=utf8 \
    && make \
    && make install \
    && pip install mecab-python3 \
    # neologd
    && cd /tools \
    && curl -SL -o mecab-ipadic-neologd-master.tar.gz ${neologd_url} \
    && tar zxf mecab-ipadic-neologd-master.tar.gz \
    && cd mecab-ipadic-neologd-master \
    && yum -y install which openssl \
    && bin/install-mecab-ipadic-neologd -n -y \
    ## cabocha
    && cd /tools \
    && curl -SL -o crfpp-master.tar.gz ${crfpp_url} \
    && tar zxf crfpp-master.tar.gz \
    && cd crfpp-master \
    && ./configure \
    && sed -i '/#include "winmain.h"/d' crf_test.cpp \
    && sed -i '/#include "winmain.h"/d' crf_learn.cpp \
    && make \
    && make install \
    && ldconfig \
    && cd /tools\
    && curl -SL -o cabocha-master.tar.gz ${cabocha_url} \
    && tar zxf cabocha-master.tar.gz \
    && cd cabocha-master \
    && autoreconf -ivf \
    && ./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8 \
    && make \
    && make install \
    && ldconfig \
    && cd python \
    && python setup.py build \
    && python setup.py install \
    ## jupyter notebook
    && yum -y install bzip2 \
    && pip install jupyter
