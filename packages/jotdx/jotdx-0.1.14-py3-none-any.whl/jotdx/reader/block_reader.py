# coding: utf-8
import struct
from jotdx.reader.base_reader import BaseReader
from collections import OrderedDict
import pandas as pd
import os
import zipfile
from io import BytesIO
"""
参考这个 http://blog.csdn.net/Metal1/article/details/44352639

"""

BlockReader_TYPE_FLAT = 0
BlockReader_TYPE_GROUP = 1

blocklist=("block_fg.dat","block_zs.dat","block_gn.dat","block.dat")
class BlockReader(BaseReader):

    def get_df(self, fname,blockfile,result_type=BlockReader_TYPE_FLAT):
        result = self.get_data(fname,blockfile, result_type)
        return pd.DataFrame(result)

    def get_data(self, fname,blockfile,result_type=BlockReader_TYPE_FLAT):
        result = []
        if type(fname) is not bytearray:
            with open(fname, "rb") as f:
                data = f.read()
        else:
            data = fname

        if blockfile in blocklist:
            pos = 384
            (num, ) = struct.unpack("<H", data[pos: pos+2])
            pos += 2
            for i in range(num):
                blockname_raw = data[pos: pos+9]
                pos += 9
                blockname = blockname_raw.decode("gbk", 'ignore').rstrip("\x00")
                stock_count, block_type = struct.unpack("<HH", data[pos: pos+4])
                pos += 4
                block_stock_begin = pos
                codes = []
                for code_index in range(stock_count):
                    one_code = data[pos: pos+7].decode("utf-8", 'ignore').rstrip("\x00")
                    pos += 7

                    if result_type == BlockReader_TYPE_FLAT:
                        result.append(
                            OrderedDict([
                                ("blockname", blockname),
                                ("block_type", block_type),
                                ("code_index", code_index),
                                ("code", one_code),
                            ])
                        )
                    elif result_type == BlockReader_TYPE_GROUP:
                        codes.append(one_code)

                if result_type == BlockReader_TYPE_GROUP:
                    result.append(
                        OrderedDict([
                            ("blockname", blockname),
                            ("block_type", block_type),
                            ("stock_count", stock_count),
                            ("code_list", ",".join(codes))
                        ])
                    )

                pos = block_stock_begin + 2800

            return result

        else:
            dat1=BytesIO(data)
            with zipfile.ZipFile(dat1,'r') as zf:
                if blockfile not in zf.namelist():
                    raise Exception('blockfile not exists')

                data0 = zf.read(blockfile)
                blockcnt,blockname,code_index,result1 = 0,'',0,[]
                data=data0.decode('gbk')
                data2=[i for i  in data.split()]
                # data3=[i[1:] for i  in data.split() if '#' in i]

                for x,i in enumerate(data2):
                    if result_type == BlockReader_TYPE_FLAT:
                        if '#' not in i :
                            result1.append(
                                OrderedDict([
                                    ("blockname", blockname),
                                    ("block_type", 2),
                                    ("code_index", code_index),
                                    ("code", i)
                                ])
                            )
                            code_index+=1
                        else :
                            blockname = i[1:]
                            code_index=0
                    elif result_type == BlockReader_TYPE_GROUP:
                        if '#' in i and x==0 :
                            blockname = i[1:]
                            codes1,blockcnt = [],0

                        elif '#' in i and x>0 :
                            result1.append(
                                OrderedDict([
                                    ("blockname", blockname),
                                    ("block_type", 2),
                                    ("stock_count", blockcnt),
                                    ("code_list", ",".join(codes1))
                                ])
                            )
                            blockname = i[1:]
                            codes1,blockcnt = [],0
                        else :
                            codes1.append(i)
                            blockcnt+=1

                return(result1)

        #从客户端取incon.dat文件
    def get_datae(self, fname,blockfile):
        result = []
        if type(fname) is not bytearray:
            with open(fname, "rb") as f:
                data = f.read()
        else:
            data = fname

        dat2=BytesIO(data)
        with zipfile.ZipFile(dat2,'r') as zf:
            if blockfile not in zf.namelist():
                raise Exception('blockfile not exists')

            data = zf.read(blockfile)
            return(data)

"""
读取通达信备份的自定义板块文件夹，返回格式与通达信板块一致，在广发证券客户端上测试通过，其它未测试
"""


class CustomerBlockReader(BaseReader):

    def get_df(self, fname, result_type=BlockReader_TYPE_FLAT):
        result = self.get_data(fname, result_type)
        return pd.DataFrame(result)

    def get_data(self, fname, result_type=BlockReader_TYPE_FLAT):

        result = []

        if not os.path.isdir(fname):
            raise Exception('not a directory')

        block_file = '/'.join([fname,'blocknew.cfg'])

        if not os.path.exists(block_file):
            raise Exception('file not exists')

        block_data = open(block_file,'rb').read()

        pos = 0
        result = []
        while pos < len(block_data):
            n1 = block_data[pos:pos + 50].decode('gbk', 'ignore').rstrip("\x00")
            n2 = block_data[pos + 50:pos + 120].decode('gbk', 'ignore').rstrip("\x00")
            pos = pos + 120

            n1 = n1.split('\x00')[0]
            n2 = n2.split('\x00')[0]
            bf = '/'.join([fname,n2 + '.blk'])
            if not os.path.exists(bf):
                raise Exception('file not exists')

            codes = open(bf).read().splitlines()
            if result_type == BlockReader_TYPE_FLAT:
                for index,code in enumerate(codes):
                    if code != '':
                        result.append(
                            OrderedDict([
                                ("blockname",n1),
                                ("block_type",n2),
                                ('code_index',index),
                                ('code',code[1:])
                            ])
                        )

            if result_type == BlockReader_TYPE_GROUP:
                cc = [c[1:] for c in codes if c != '']
                result.append(
                    OrderedDict([
                        ("blockname",n1),
                        ("block_type",n2),
                        ("stock_count",len(cc)),
                        ("code_list",",".join(cc))
                    ])
                )

        return result


if __name__ == '__main__':
    df2 = pd.DataFrame(BlockReader().get_df("C:\\new_jyplug\\T0002\\hq_cache\\block_zs.dat", "block_zs.dat", BlockReader_TYPE_GROUP))
    # data2=set([i for i in df2.blockname ])
    # df3 = CustomerBlockReader().get_df('C:/Users/fit/Desktop/blocknew')
    # print(df3)
    # df4 = CustomerBlockReader().get_df('C:/Users/fit/Desktop/blocknew',BlockReader_TYPE_GROUP)
    print(df2.loc[:,:1000])
