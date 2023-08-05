# kong-control-plane

[![NPM version](https://badge.fury.io/js/kong-control-plane.svg)](https://badge.fury.io/js/kong-control-plane)
[![PyPI version](https://badge.fury.io/py/kong-control-plane.svg)](https://badge.fury.io/py/kong-control-plane)

![Downloads](https://img.shields.io/badge/-DOWNLOADS:-brightgreen?color=gray)
![npm](https://img.shields.io/npm/dt/kong-control-plane?label=npm&color=orange)
![PyPI](https://img.shields.io/pypi/dm/kong-control-plane?label=pypi&color=blue)

Use this Kong CDK Construct Library to deploy Kong control plane on Amazon EKS .

This CDK library automatically creates and configures recommended architecture on AWS by:

* *Amazon EKS*

  * Well architected EKS cluster from networking standpoint
  * Cluster autoscaler
  * Node termination handler
  * Secrets management from AWS Secrets Manager using CSI driver
  * mTLS using AWS ACM for pod to pod communication using private certificate authority and aws-pca-issuer
  * Use of IAM Role for Service Account (IRSA) where applicable
  * AWS EKS encryption at rest
  * Metrics server installation
  * Logs and metrics to cloudwatch using AWS CloudWatch Container insights
* *Elasticache*

  * private accessibility
  * multi az
  * auto failover
  * auto minor version upgrade
  * cwl output
* *RDS Features*

  * Encryption at rest
  * Private subnets
  * Multiaz
  * auto backup
  * Logs output to CloudWatch

## npm Package Installation:

```
yarn add --dev kong-control-plane
# or
npm install kong-control-plane --save-dev
```

## PyPI Package Installation:

```
pip install kong-control-plane
```

# Sample

Try out https://github.com/kong/aws-samples for the complete sample application and instructions.

## Resources to learn about CDK

* [CDK TypeScript Workshop](https://cdkworkshop.com/20-typescript.html)
* [Video Introducing CDK by AWS with Demo](https://youtu.be/ZWCvNFUN-sU)
* [CDK Concepts](https://youtu.be/9As_ZIjUGmY)

## Related

Kong on AWS Hands on Workshop - https://kong.awsworkshop.io/
Kong Data plane on AWS contruct - FILLME
