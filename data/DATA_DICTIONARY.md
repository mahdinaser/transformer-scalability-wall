# Data Dictionary: Transformer Scalability Crisis Dataset

This document provides detailed descriptions of all data files and their columns in the Transformer Scalability Crisis dataset.

## 📋 Overview

The dataset contains 10 primary data tables documenting the performance characteristics of 118 transformer models across 7 architectural categories. Each table captures different aspects of model performance, scalability, and efficiency.

---

## 📊 Table 1: Model Loading and Memory Usage Analysis
**File:** `table1_model_loading.csv`

### Description
Comprehensive analysis of resource requirements during model initialization and base memory consumption.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Model` | string | Model identifier/name | - | 118 unique models |
| `Parameters (M)` | float | Total model parameters | Millions | 11.7 - 7069.0 |
| `Loading Time (s)` | float | Model initialization time | Seconds | 0.20 - 641.98 |
| `Memory Used (GB)` | float | Base memory consumption | Gigabytes | -6.98 - 3.18 |
| `Memory/Param (MB/M)` | float | Memory efficiency ratio | MB per M params | -12.0 - 233.0 |

### Notes
- Negative memory values indicate measurement artifacts or baseline adjustments
- Loading time includes model weight loading and initialization
- Memory measurements taken at model load completion

---

## 🚀 Table 2: Inference Speed Analysis  
**File:** `table2_inference_speed.csv`

### Description
Systematic throughput evaluation across different sequence lengths revealing scalability limitations.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Model` | string | Model identifier | - | 118 unique models |
| `128 tok/s` | mixed | Throughput at 128 tokens | Tokens/second | 50 - 25155, "OOM" |
| `512 tok/s` | mixed | Throughput at 512 tokens | Tokens/second | 458 - 101908, "OOM" |
| `1024 tok/s` | mixed | Throughput at 1024 tokens | Tokens/second | 266 - 176390, "OOM" |

### Special Values
- `OOM`: Out of Memory - model failed at this sequence length
- Numeric values: Successful throughput measurement

### Key Insights
- 88.1% success rate at 512 tokens
- 44.9% success rate at 1024 tokens  
- 0% success rate at 2048 tokens (universal failure)

---

## 💾 Table 3: Memory Scaling Analysis
**File:** `table3_memory_scaling.csv`

### Description
Memory consumption patterns across sequence lengths with scaling factor calculations.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Model` | string | Model identifier | - | 118 unique models |
| `128 Memory` | string | Memory at 128 tokens | GB or "N/A" | Currently "N/A" |
| `512 Memory` | string | Memory at 512 tokens | GB or "N/A" | Currently "N/A" |
| `1024 Memory` | string | Memory at 1024 tokens | GB or "N/A" | Currently "N/A" |
| `Scaling Factor` | string | Memory scaling coefficient | Multiplier or "N/A" | Currently "N/A" |

### Notes
- Current version shows "N/A" values - indicates data collection in progress
- Scaling factor represents memory growth rate with sequence length
- Critical for understanding memory bottlenecks

---

## ⚡ Table 4: Comprehensive Efficiency Analysis
**File:** `table4_efficiency.csv`

### Description
Multi-dimensional efficiency metrics combining throughput, memory, and parameter considerations.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Model` | string | Model identifier | - | 118 unique models |
| `Params (M)` | float | Model parameters | Millions | 11.7 - 7069.0 |
| `Memory (GB)` | float | Memory consumption | Gigabytes | -6.98 - 3.18 |
| `Throughput@512` | mixed | Speed at 512 tokens | Tokens/second | 458 - 101908, "N/A" |
| `Throughput/Param` | float | Parameter efficiency | Tok/s per M params | 0.0 - 4645.77 |
| `Params/GB` | float | Memory efficiency | M params per GB | 0.0 - 247334.7 |
| `Overall Score` | float | Composite efficiency metric | Unitless | 0.0 - 29883082.55 |

### Efficiency Categories
1. **Compressed Models:** 649.2 tok/s/M (highest)
2. **BERT Family:** 233.0 tok/s/M  
3. **Efficient Transformers:** 42.9 tok/s/M
4. **Generative LLM:** 12.5 tok/s/M
5. **Small LLM:** 0.6 tok/s/M (lowest)

---

## 📏 Table 5: Scalability Classification Framework
**File:** `table5_scalability.csv`

### Description
Novel taxonomy classifying models by maximum operational sequence length and architectural characteristics.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Model` | string | Model identifier | - | 118 unique models |
| `Max Seq Length` | integer | Maximum sequence length | Tokens | 128 - 2048 |
| `Scaling Complexity` | string | Theoretical complexity | Category | Linear, Quadratic, Limited |
| `Architecture Type` | string | Model category | Category | 7 categories |
| `Efficiency Rating` | string | Performance tier | Category | Very Low, Low, Medium, High |

### Architecture Types
- **BERT Family:** Encoder-only models (34 models)
- **Generative LLM:** Autoregressive models (50 models)  
- **Compressed:** Distilled/compressed variants (5 models)
- **Efficient Transformer:** Long-sequence optimized (4 models)
- **Small LLM:** Compact language models (4 models)
- **Code Model:** Programming-specialized (2 models)
- **Other:** Miscellaneous architectures (19 models)

---

## 📊 Table 6: Category Comparison Summary
**File:** `table6_category_comparison.csv`

### Description
Aggregated performance statistics by architectural category for high-level comparisons.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Category` | string | Architecture category | - | 7 categories |
| `Model Count` | integer | Models in category | Count | 1 - 50 |
| `Avg Params (M)` | float | Average parameters | Millions | 139.4 - 1012.1 |
| `Avg Load Time (s)` | float | Average loading time | Seconds | 0.52 - 5.21 |
| `Avg Speed@512 (tok/s)` | integer | Average throughput | Tokens/second | 2650 - 3922 |
| `Avg Max Seq Length` | integer | Average max sequence | Tokens | 512 - 1638 |
| `Best Model` | string | Top performer | Model name | Category-specific |

---

## 🎯 Table 7: Dataset Performance Analysis
**File:** `table7_dataset_performance.csv`

### Description
Performance evaluation across standard NLP datasets showing task-specific capabilities.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Model` | string | Model identifier | - | 36 models tested |
| `imdb` | integer | IMDB sentiment score | Score | 20 |
| `glue` | integer | GLUE benchmark score | Score | 20 |
| `yelp` | integer | Yelp sentiment score | Score | 20 |
| `squad` | integer | SQuAD QA score | Score | 20 |
| `Avg Speed@512` | integer | Average throughput | Tokens/second | 143 - 14311 |
| `Success Rate` | float | Task completion rate | Percentage | 20.0% |
| `Datasets Working` | string | Compatible datasets | Fraction | "7/8" |

### Dataset Types
- **IMDB:** Movie review sentiment analysis
- **GLUE:** General Language Understanding Evaluation
- **Yelp:** Business review sentiment  
- **SQuAD:** Reading comprehension Q&A

---

## 🔧 Table 8: Task Type Analysis
**File:** `table8_task_type_analysis.csv`

### Description
Detailed performance breakdown across 14 different NLP task categories.

### Columns
| Column | Type | Description | Units | Example |
|--------|------|-------------|-------|---------|
| `Model` | string | Model identifier | - | distilbert-base-uncased |
| `Sentiment` | string | Sentiment analysis perf | "speed (success%)" | "11328 (100.0%)" |
| `Grammar` | string | Grammar checking perf | "speed (success%)" | "11254 (100.0%)" |
| `Paraphrase` | string | Paraphrase detection | "speed (success%)" | "11269 (100.0%)" |
| `Qa` | string | Question answering | "speed (success%)" | "11286 (100.0%)" |
| `Lm` | string | Language modeling | "speed (success%)" | "11164 (100.0%)" |
| `Long_text` | string | Long text processing | "speed (success%)" | "11225 (100.0%)" |
| `Summarization` | string | Text summarization | "speed (success%)" | "11126 (100.0%)" |
| `Translation` | string | Machine translation | "speed (success%)" | "11163 (100.0%)" |
| `Code` | string | Code understanding | "speed (success%)" | "11208 (100.0%)" |
| `Financial` | string | Financial text analysis | "speed (success%)" | "11200 (100.0%)" |
| `Conversation` | string | Dialogue systems | "speed (success%)" | "11190 (100.0%)" |
| `Medical` | string | Medical text processing | "speed (success%)" | "11158 (100.0%)" |
| `Science` | string | Scientific text analysis | "speed (success%)" | "11116 (100.0%)" |
| `Multilingual` | string | Multi-language tasks | "speed (success%)" | "11214 (100.0%)" |

### Value Format
Each cell contains: `throughput (success_rate%)`
- **Throughput:** Tokens processed per second
- **Success Rate:** Percentage of successful completions

---

## 📐 Table 9: Sequence Length Capabilities
**File:** `table9_sequence_capabilities.csv`

### Description
Maximum working sequence length determination with success/failure patterns across lengths.

### Columns
| Column | Type | Description | Units | Format |
|--------|------|-------------|-------|--------|
| `Model` | string | Model identifier | - | Model name |
| `128` | string | 128-token performance | "✓ speed" or "✗ OOM" | "✓ 5866" |
| `512` | string | 512-token performance | "✓ speed" or "✗ OOM" | "✓ 11213" |
| `1024` | string | 1024-token performance | "✓ speed" or "✗ OOM" | "✗ OOM" |
| `2048` | string | 2048-token performance | "✓ speed" or "✗ OOM" | "✗ OOM" |
| `Max Working Length` | integer | Maximum successful length | Tokens | 512, 1024, 2048 |
| `Architecture Type` | string | Model category | Category | 7 categories |

### Status Indicators
- **✓ [number]:** Successful with throughput measurement
- **✗ OOM:** Out of Memory failure

### Scalability Patterns
- **512 tokens:** 88.1% success rate
- **1024 tokens:** 44.9% success rate (51% drop)
- **2048 tokens:** 0% success rate (universal failure)

---

## 🎯 Table 10: Dataset Difficulty Analysis
**File:** `table10_dataset_difficulty.csv`

### Description
Ranking of 25 NLP datasets by computational difficulty and model compatibility.

### Columns
| Column | Type | Description | Units | Range |
|--------|------|-------------|-------|-------|
| `Rank` | integer | Difficulty ranking | Position | 1 - 25 |
| `Dataset` | string | Dataset name | - | 25 datasets |
| `Task Type` | string | Primary task category | Category | 8 task types |
| `Success Rate` | float | Model success percentage | Percentage | 20.0% - 26.7% |
| `Avg Speed (tok/s)` | integer | Average throughput | Tokens/second | 3190 - 3348 |
| `Models Tested` | integer | Number of models evaluated | Count | 34 |
| `Difficulty` | string | Difficulty classification | Category | "Very Hard" |

### Task Categories
- **Sentiment:** Sentiment analysis tasks
- **Grammar:** Grammar and linguistic tasks  
- **Paraphrase:** Paraphrase detection
- **QA:** Question answering
- **LM:** Language modeling
- **Long_Text:** Long document processing
- **Summarization:** Text summarization
- **Translation:** Machine translation
- **Code:** Code understanding
- **Financial:** Financial text analysis
- **Conversation:** Dialogue tasks
- **Medical:** Medical text processing
- **Science:** Scientific text analysis
- **Multilingual:** Cross-lingual tasks

---

## 🔍 Data Quality Notes

### Missing Values
- Some tables contain "N/A" values indicating ongoing data collection
- "OOM" indicates legitimate Out of Memory failures, not missing data
- Negative values in memory measurements may indicate baseline adjustments

### Measurement Precision
- **Throughput:** Measured in tokens per second with sub-second precision
- **Memory:** Measured in GB with 0.01 GB precision
- **Parameters:** Counted in millions with 0.1M precision
- **Loading Time:** Measured in seconds with millisecond precision

### Reproducibility
- All measurements conducted on standardized Mac GPU (MPS) hardware
- Multiple runs averaged for statistical stability
- Consistent evaluation protocol across all models

---

## 📈 Usage Examples

### Loading Efficiency Analysis
```python
import pandas as pd

# Load the data
loading_df = pd.read_csv('table1_model_loading.csv')

# Find most efficient loaders
efficient_models = loading_df.nsmallest(10, 'Loading Time (s)')
print("Fastest loading models:")
print(efficient_models[['Model', 'Loading Time (s)', 'Parameters (M)']])
```

### Scalability Wall Analysis  
```python
# Load inference speed data
speed_df = pd.read_csv('table2_inference_speed.csv')

# Count successful models at each sequence length
seq_lengths = ['128 tok/s', '512 tok/s', '1024 tok/s']
success_rates = {}

for length in seq_lengths:
    successful = speed_df[speed_df[length] != 'OOM'].shape[0]
    total = speed_df.shape[0]
    success_rates[length] = (successful / total) * 100
    
print("Success rates by sequence length:")
for length, rate in success_rates.items():
    print(f"{length}: {rate:.1f}%")
```

### Category Performance Comparison
```python
# Load efficiency data
efficiency_df = pd.read_csv('table4_efficiency.csv')

# Calculate category averages (need to map models to categories)
category_performance = efficiency_df.groupby('Category').agg({
    'Throughput/Param': 'mean',
    'Params (M)': 'mean',
    'Overall Score': 'mean'
}).round(2)

print("Performance by category:")
print(category_performance)
```

---

This data dictionary provides the foundation for understanding and analyzing the comprehensive transformer scalability dataset. Each table contributes unique insights into the performance characteristics and limitations of modern transformer architectures.
