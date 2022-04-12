[![MIT License](https://img.shields.io/badge/License-MIT-lightgray.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.8.5-blue.svg)
<!-- Add in additional badges as appropriate -->

![Banner of NHS AI Lab Skunkworks ](docs/banner.png)

# NHS AI Lab Skunkworks project: Length of Stay baseline predictive models

> A internal capability project for the NHS AI (Artificial Intelligence) Lab Skunkworks team, Length of Stay baseline predictive models seeks to provide simple baseline models for predicting length of stay (days) in a secondary care setting.

Length of Stay baseline predictive models was selected as a project to run in tandem with the [NHS AI Lab Skunkworks project: Long Stayer Risk Stratification](https://github.com/nhsx/skunkworks-long-stayer-risk-stratification), and started in March 2022.

## Intended Use

The work contained in this repository is experimental research and is intended to demonstrate the technical validity of applying machine learning models to medical records datasets in order to predict length of stay. It is not intended for deployment in a clinical or non-clinical setting without further development and compliance with the [UK Medical Device Regulations 2002](https://www.legislation.gov.uk/uksi/2002/618/contents/made) where the product qualifies as a medical device.

## Data Protection

This project was subject to a Data Protection Impact Assessment (DPIA), ensuring the protection of the data used in line with the [UK Data Protection Act 2018](https://www.legislation.gov.uk/ukpga/2018/12/contents/enacted) and [UK GDPR](https://ico.org.uk/for-organisations/dp-at-the-end-of-the-transition-period/data-protection-and-the-eu-in-detail/the-uk-gdpr/). No data or trained models are shared in this repository.

## Background

Hospital long stayers, those with a length of stay (LoS) of 21 days or longer, have significantly worse medical and social outcomes than other patients. Long-stayers are often medically optimised (fit for discharge) many days before their actual discharge. Moreover, there are a complex mixture of medical, cultural and socioeconomic factors which contribute to the causes of unnecessary long stays.

The AI Lab Skunkworks team commissioned a [Long Stayer Risk Stratification](https://github.com/nhsx/skunkworks-long-stayer-risk-stratification) model in April 2021 using some approaches from Generative Adversarial Networks (GANs), including a Convolutional Neural Network (CNN) to predict Length of Stay.

This project aims to complement that work with simpler baseline models that could be replicated at other hospital trusts.

## Model selection

_Include a high-level rationale of the approach you took._

## Known limitations

_Include known limitations and issues with your approach._

## Data pipeline

_Include an ideally visual representation of data flow, and include a link to a data dictionary/data requirements._

## Getting Started

1. Create a new virtual environment e.g. `pyenv virtualenv 3.8.5 long-stay-baseline`
2. Activate your environment e.g. `pyenv activate long-stay-baseline`
3. Install required packages: `pip install -r requirements.txt`
4. **Activate the git pre commit hook: `pre-commit install`**

_Include a brief overview of the codebase. Include setup and execution instructions, including any required environment variables.

## NHS AI Lab Skunkworks

The project is supported by the NHS AI Lab Skunkworks, which exists within the NHS AI Lab at the NHS Transformation Directorate to support the health and care community to rapidly progress ideas from the conceptual stage to a proof of concept.

Find out more about the [NHS AI Lab Skunkworks](https://www.nhsx.nhs.uk/ai-lab/ai-lab-programmes/skunkworks/).
Join our [Virtual Hub](https://future.nhs.uk/connect.ti/system/text/register) to hear more about future problem-sourcing event opportunities.
Get in touch with the Skunkworks team at [aiskunkworks@nhsx.nhs.uk](aiskunkworks@nhsx.nhs.uk).

## Licence

Unless stated otherwise, the codebase is released under [the MIT Licence][mit].
This covers both the codebase and any sample code in the documentation.

The documentation is [© Crown copyright][copyright] and available under the terms
of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
