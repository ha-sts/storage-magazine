Storage Magazine
================

Component of the storage layer that will hold the data at rest.

Ideas
-----

 * Should the storage folders use two, three, or four digits?  Leaning toward three for funsies.

 * Put marker files at the locations for other hashes that point to the location of the actual file:
```
storage_directory
 |_ sha256
 |   |_ 012
 |   |   \_ <full_sha256>.binary
 |   \_ abc
 |       \_ <full_sha256>.binary
 \_ sha512
     |_ 321
     |   \_ <full_sha512>.marker
     \_ dcb
         \_ <full_sha512>.marker
```

 * Markers contain the primary storage hash of the binary:
```
sha256_<full_sha256>
```

 * Figure out how to do chunked upload (per HTTP 1.1):
   https://www.rfc-editor.org/rfc/rfc9112#name-chunked-transfer-coding

 * Figure out how to do multipart upload (AWS type, not HTTP).  Here's a post explaining their multipart upload:
   https://aws.amazon.com/blogs/compute/uploading-large-objects-to-amazon-s3-using-multipart-upload-and-transfer-acceleration/
