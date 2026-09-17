# Provenance and third-party materials

This repository is a curated edition of the quantitative-finance agent benchmark originally developed collaboratively at Varsity Tech. It is maintained by Syx403 and retains contributions from Rick Chan and the original team.

The core snapshot is based on source revision `45acc55d252d19c7df996e24d9cd574686dced8d` from May 6, 2026. Publication cleanup removes retired runtimes, planning archives, company deployment configuration, local credentials, and generated run output. Documentation and retained tests are aligned with the included implementation.

The simulator study uses six fixed task fixtures recovered from the pre-migration task tree at `587856f7^`; they are stored with the experiment so its original design remains reproducible without restoring the obsolete runtime. The small calibration fixture retains numeric scores and matching keys, with transcript text and reviewer identities omitted.

## Dependencies and data

- QuantConnect LEAN is an external engine. The optional Docker build obtains its source at the pinned revision in `Dockerfile.lean`; its upstream license and notices apply.
- Model SDKs, MCP, Python packages, and other dependencies retain their respective licenses.
- Knowledge tasks include material selected from financial QA sources such as FiQA, FinQA, ConvFinQA, and TAT-QA, as well as cited reference sources. Task metadata preserves provenance. Those sources and any external market data retain their own terms.
- Large historical market datasets and full experiment transcripts are not redistributed in this repository.

This notice records attribution and does not replace upstream licenses or grant additional rights to third-party material.
