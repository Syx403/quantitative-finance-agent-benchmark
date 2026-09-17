# Running the benchmark

[Back to the project](../README.md)

## Local setup

Run commands from the repository root. Install `requirements-dev.txt` for development, or `requirements.txt` for the runtime alone.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/check_catalog.py
python -m pytest -q
```

The default tests block outbound network access and use mocked model/data services. They test application behavior without consuming model credits.

## Credentials and configuration

Copy `.env.example` to `.env`. Live simulation and judging use `OPENROUTER_API_KEY`. The default baseline client is also configured for OpenRouter; native Anthropic and Claude Agent SDK modes are optional paths configured in [`bench/client/adapters/config.py`](../bench/client/adapters/config.py).

| Setting | Where |
| --- | --- |
| Baseline model and API routing | `bench/client/adapters/config.py` |
| Simulator and evaluator defaults | `bench/server/config/llm_config.py` |
| Experiment model panel | `bench/server/config/llm_config.py` |
| Task-specific tools, networking, and image | Individual task JSON |
| Dataset repository and revision | `bench/server/config/benchmark_config.py` |
| Optional service credentials | `.env.example` |

Model identifiers and cost tables reflect the original snapshot. Check provider availability and pricing before a live run. The optional Claude Agent SDK path requires installing `claude-agent-sdk`; it is not needed for the default API-based client.

## Sandbox images

Build the standard image for Python analysis and code tasks:

```bash
docker build -f bench/docker/Dockerfile \
  -t quant-bench-env:v3.0 -t quant-tutor-env:v2.2 bench
```

For LEAN/C# tasks, build the additional image after the standard image. The build downloads and compiles a pinned LEAN revision and can take substantial time and disk space.

```bash
docker build -f bench/docker/Dockerfile.lean \
  -t quant-bench-env:v3.0-lean -t quant-tutor-env:v2.2-lean bench
```

The build context must be `bench`, because the LEAN Dockerfile copies files from `docker/` and `scripts/`.

## Start the server

```bash
PYTHONPATH=bench python -m server --host 127.0.0.1 --port 8000 --docker
```

In another terminal:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/client/tasks/catalog/labels
```

Open `http://127.0.0.1:8000` for the dashboard. `/mcp` is the Streamable HTTP MCP endpoint; `/session/*` exposes the REST session interface.

For application development with trusted fixtures, `--no-docker` runs tools locally. That mode does not isolate agent code. The local example binds to loopback and disables hosted-user authentication. Configure authentication and separate client/admin credentials before exposing a deployment to other users.

## Run the baseline client

After configuring a model key and starting the server:

```bash
PYTHONPATH=bench python -m client run \
  --server http://127.0.0.1:8000 \
  --protocol rest \
  --task L2_ADV_01_investment_advice
```

Use `--protocol mcp` for the MCP transport. `python -m client run --help`, with `PYTHONPATH=bench`, lists the available options. Live execution includes model calls for the agent, simulated user, and applicable judges.

To attach to an existing Run, use the execution token returned when the Run was created:

```bash
PYTHONPATH=bench python -m client attach \
  --server http://127.0.0.1:8000 \
  --protocol rest \
  --run-token YOUR_RUN_EXECUTION_TOKEN
```

## Connect an external agent

The baseline client is optional. An external client follows the same lifecycle:

1. Select a label from `GET /client/tasks/catalog/labels`.
2. Create an attempt through `POST /client/runs/start` with a `task` field. Authenticated deployments require the configured client credential.
3. Use the returned execution token for the Session/MCP connection. Keep the owner control token separate.
4. Register and start the Session. Discover the allowed tools and read the task context.
5. Call tools and `send_message` as needed. Respect phase errors and the completion response.
6. Retrieve saved results and evaluation status. Evaluation management is a separate server/operator responsibility.

The implementation contract lives in [`protocol.py`](../bench/server/api/protocol.py). Example transports are in [`bench/client/transports/`](../bench/client/transports).

## Task data and outputs

Task definitions are tracked; large market datasets are not. The reference environment retains a pinned Hugging Face dataset configuration. Live data-backed tasks require access to that dataset or equivalent local inputs. LEAN metadata and small runtime fixtures are included under `bench/runtime_assets/`.

[`gen_v3_data.py`](../bench/scripts/gen_v3_data.py) generates additional seeded inputs and buggy code examples; it requires its BTC reference input first. It is not a replacement for the complete historical dataset.

Generated data, results, and credentials remain local and are ignored by Git. Saved Session results include conversation/tool records and workspace artifacts. Repeated evaluations create versioned score records. See the [evaluation guide](evaluation.md) for their interpretation.
