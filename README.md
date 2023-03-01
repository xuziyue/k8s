# k8s

apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        name: main-route 
      target:
        type : Value 
        value : "2k"
  behavior:
    scaleDown:
      stabilizationWindowSeconds :300 
      policies :
       - type : Pods 
         value :4 
         periodSeconds :60 

This YAML file creates an HPA named nginx that targets a deployment named nginx. It specifies a minimum of 1 replica and a maximum of 10 replicas. The HPA scales based on two metrics:

1. CPU utilization with a target average utilization of 50%
2. A custom metric named requests-per-second associated with an Ingress object named main-route, with a target value of "2k"

The scaling behavior is also defined, specifying that when scaling down, there should be a stabilization window of 300 seconds and a maximum scale down rate of 4 pods every 60 seconds.

You can apply this YAML file using kubectl apply -f <filename>.yaml.
