# Testing & CI for GenAI Applications

Build and test AI applications with confidence. This repository contains examples and starter code from our workshop on implementing reliable testing practices for generative AI systems.

Workshop recording, you can follow along yourself: [video](https://www.youtube.com/watch?v=Wz1HXUBSThA)

## What's Inside

The code demonstrates three key patterns for testing AI applications:

1. `comedian.yaml` shows how to test for consistent AI personality and behavior. We use a simple comedian bot to demonstrate how automated testing can drive prompt engineering.

2. `hr-docs.yaml` demonstrates testing document Q&A capabilities by connecting to a knowledge base of HR policies and verifying response accuracy.

3. `exchange-rates.yaml` showcases API integration testing, ensuring proper handling of user inputs like currency pairs and focused, relevant responses.

## Quick Start

```bash
# Install Helix CLI
curl https://deploy.helix.ml/install.sh | bash

# Deploy an app
helix apply -f comedian.yaml

# Run tests
helix test -f comedian.yaml
```

## Setting Up CI

The repository includes GitHub Actions and GitLab CI configurations to automatically test your AI applications on every commit. See `.github/workflows/helix.yml` for a complete example of:
- Running tests on pull requests
- Automated deployment on merge to main
- Test report generation and PR comments

## Learn More

- Watch the workshop recording: [video](https://www.youtube.com/watch?v=Wz1HXUBSThA)
- Join our next workshop, check the blog: https://blog.helix.ml/
- Try Helix: https://deploy.helix.ml/

Questions? Join us on [Discord](https://discord.gg/VJftd844GE) or the [MLOps Community Slack](https://gatewaze.mlops.community/) #helix channel.
