﻿#Encrypt by Muzacky #Gitlab : https://github.com/Muzacky02/muzacky/tree/master import marshal,zlib,base64 exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
