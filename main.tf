module "backend_infrastructure" {
    source = "./backend_infrastructure"
    integration_uri = var.integration_uri
}

module "frontend_infrastructure" {
  source = "./frontend_infrastructure"
}
