resource "aws_cloudfront_distribution" "my_distribution" {
  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = ""
  price_class         = "PriceClass_All"

  aliases = ["princetonabdulsalam.cloud"]

  origin {
    domain_name = "princetonabdulsalam.cloud.s3-website-us-east-1.amazonaws.com"
    origin_id   = "princetonabdulsalam.cloud.s3-website-us-east-1.amazonaws.com"
    
    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "http-only"
      origin_ssl_protocols   = ["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]
    }
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "princetonabdulsalam.cloud.s3-website-us-east-1.amazonaws.com"

    cache_policy_id = "658327ea-f89d-4fab-a63d-7e88639e58f6"  # This is the Managed-CachingOptimized policy ID

    viewer_protocol_policy = "redirect-to-https"
    compress               = true
    
    # Remove the forwarded_values block
    # Remove min_ttl, default_ttl, and max_ttl
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = aws_acm_certificate.princetonabdulsalam_cloud.arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }
  # ensures the distribution waits for the certificate to be validated
  depends_on = [aws_s3_bucket.princetonabdulsalam,
  aws_acm_certificate.princetonabdulsalam_cloud,
  ]
}