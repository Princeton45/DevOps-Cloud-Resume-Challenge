# This block will configure the directory to point to the specific workspace

terraform {
  cloud {
    organization = "Cloud-Organization"
    workspaces {
      name = "Iman-Renner-AWS-cloud-resume-env"
    }
  }
}
