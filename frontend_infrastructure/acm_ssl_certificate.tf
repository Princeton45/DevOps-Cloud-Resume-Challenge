resource "aws_acm_certificate" "princetonabdulsalam_cloud" {
  domain_name               = "princetonabdulsalam.cloud"
  subject_alternative_names = ["*.princetonabdulsalam.cloud"]
  validation_method         = "DNS"  # or "EMAIL", depending on your preference
  
  /*
  When you need to update or rotate certificates,
   create_before_destroy allows you to create a new certificate before destroying 
   the old one. This ensures continuous availability of a valid certificate.
  */
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [ aws_s3_bucket.princetonabdulsalam ]

}