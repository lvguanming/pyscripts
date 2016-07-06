# -*- coding: utf-8 -*-
# flake8: noqa

# from qiniu import Auth, put_file, etag, urlsafe_base64_encode
# import qiniu.config
# import os
#
# access_key = '1lKyl7'
# secret_key = 'aReElm'
# q = Auth(access_key, secret_key)
# bucket_name = 'lvgm'
# #token = q.upload_token(bucket_name, key, 3600)
# localfileDir = '/data/articles'
#
# if __name__ == "__main__":
# 	print "hahaha"
# 	files = [f for f in os.listdir(localfileDir) if os.path.isfile(os.path.join(localfileDir, f))]
# 	for file in files:
# 		f = localfileDir + "/" + file
# 		print f
# 		token = q.upload_token(bucket_name, f.replace('/data/',''), 3600)
# 		ret, info = put_file(token, f.replace('/data/',''), f)
# 		if ret is not None:
# 			print "Put Ok : {}".format(file)
# 		else:
# 			print "Error: {}".format(file)
# 			print(info)
