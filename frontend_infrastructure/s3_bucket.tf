resource "aws_s3_bucket" "princetonabdulsalam" {
  bucket = "princetonabdulsalam.cloud"
}

resource "aws_s3_bucket_website_configuration" "princetonabdulsalam_website" {
  bucket = aws_s3_bucket.princetonabdulsalam.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
  depends_on = [ aws_s3_bucket.princetonabdulsalam ]
}