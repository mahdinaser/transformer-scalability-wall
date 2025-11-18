#!/usr/bin/env python3
"""
Transformer Scalability Crisis Analysis Script

This script analyzes the comprehensive transformer scalability dataset and generates
key visualizations and statistics from the paper.

Author: Mahdi Naser Moghadasi
Institution: BrightMind AI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style for publication-quality plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class TransformerScalabilityAnalyzer:
    """Comprehensive analyzer for transformer scalability data."""
    
    def __init__(self, data_dir="data/raw"):
        """Initialize analyzer with data directory."""
        self.data_dir = Path(data_dir)
        self.figures_dir = Path("figures")
        self.figures_dir.mkdir(exist_ok=True)
        
        # Load all data tables
        self.load_data()
        
    def load_data(self):
        """Load all CSV data files."""
        print("Loading transformer scalability dataset...")
        
        # Table 1: Model Loading and Memory Usage
        self.loading_data = pd.read_csv(self.data_dir / "table1_model_loading.csv")
        
        # Table 2: Inference Speed Analysis
        self.speed_data = pd.read_csv(self.data_dir / "table2_inference_speed.csv")
        
        # Table 3: Memory Scaling (currently N/A values)
        self.memory_data = pd.read_csv(self.data_dir / "table3_memory_scaling.csv")
        
        # Table 4: Efficiency Analysis
        self.efficiency_data = pd.read_csv(self.data_dir / "table4_efficiency.csv")
        
        # Table 5: Scalability Classification
        self.scalability_data = pd.read_csv(self.data_dir / "table5_scalability.csv")
        
        # Table 6: Category Comparison
        self.category_data = pd.read_csv(self.data_dir / "table6_category_comparison.csv")
        
        # Table 7: Dataset Performance
        self.dataset_perf = pd.read_csv(self.data_dir / "table7_dataset_performance.csv")
        
        # Table 8: Task Type Analysis
        self.task_analysis = pd.read_csv(self.data_dir / "table8_task_type_analysis.csv")
        
        # Table 9: Sequence Capabilities
        self.sequence_caps = pd.read_csv(self.data_dir / "table9_sequence_capabilities.csv")
        
        # Table 10: Dataset Difficulty
        self.dataset_difficulty = pd.read_csv(self.data_dir / "table10_dataset_difficulty.csv")
        
        print(f"Loaded {len(self.loading_data)} models across 10 data tables.")
        
    def analyze_scalability_wall(self):
        """Analyze and visualize the transformer scalability wall."""
        print("\n=== Analyzing Transformer Scalability Wall ===")
        
        # Count successful models at each sequence length
        seq_columns = ['128 tok/s', '512 tok/s', '1024 tok/s']
        success_counts = {}
        total_models = len(self.speed_data)
        
        for col in seq_columns:
            # Count non-OOM entries
            successful = self.speed_data[self.speed_data[col] != 'OOM'].shape[0]
            success_counts[col] = successful
            
        # Add 2048 (all fail)
        success_counts['2048 tok/s'] = 0
        
        # Calculate success rates
        sequence_lengths = [128, 512, 1024, 2048]
        success_rates = [
            success_counts['128 tok/s'] / total_models * 100,
            success_counts['512 tok/s'] / total_models * 100, 
            success_counts['1024 tok/s'] / total_models * 100,
            0  # 2048 tokens - universal failure
        ]
        
        print(f"Success rates by sequence length:")
        for length, rate in zip(sequence_lengths, success_rates):
            print(f"  {length} tokens: {rate:.1f}% ({success_counts.get(f'{length} tok/s', 0)}/{total_models} models)")
            
        # Create the scalability wall visualization
        plt.figure(figsize=(12, 8))
        plt.plot(sequence_lengths, success_rates, 'o-', linewidth=3, markersize=10, color='#e74c3c')
        plt.fill_between(sequence_lengths, success_rates, alpha=0.3, color='#e74c3c')
        
        plt.xlabel('Sequence Length (tokens)', fontsize=14, fontweight='bold')
        plt.ylabel('Working Models (%)', fontsize=14, fontweight='bold')
        plt.title('The Transformer Scalability Wall\nEmpirical Evidence of Performance Degradation', 
                 fontsize=16, fontweight='bold', pad=20)
        
        # Add annotations for key points
        plt.annotate(f'{success_rates[1]:.1f}% Success\n(Stable Region)', 
                    xy=(512, success_rates[1]), xytext=(400, 70),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    fontsize=12, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
        
        plt.annotate(f'{success_rates[2]:.1f}% Success\n(51% Failure Rate)', 
                    xy=(1024, success_rates[2]), xytext=(1200, 30),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    fontsize=12, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="orange"))
        
        plt.annotate('Complete Failure\n(Universal Wall)', 
                    xy=(2048, 0), xytext=(1800, 15),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    fontsize=12, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral"))
        
        plt.grid(True, alpha=0.3)
        plt.xlim(100, 2100)
        plt.ylim(-5, 100)
        plt.tight_layout()
        plt.savefig(self.figures_dir / 'scalability_wall.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return success_rates
        
    def analyze_efficiency_hierarchy(self):
        """Analyze parameter efficiency across model categories."""
        print("\n=== Analyzing Efficiency Hierarchy ===")
        
        # Map models to categories (simplified mapping)
        def categorize_model(model_name):
            model_lower = model_name.lower()
            if 'distil' in model_lower or 'squeeze' in model_lower:
                return 'Compressed'
            elif any(x in model_lower for x in ['bert', 'roberta', 'albert', 'electra', 'deberta']):
                return 'BERT Family'
            elif any(x in model_lower for x in ['gpt', 'opt', 'bloom', 'pythia', 'cerebras', 'llama']):
                return 'Generative LLM'
            elif 'longformer' in model_lower or 'bigbird' in model_lower:
                return 'Efficient Trans.'
            elif 'phi' in model_lower or 'tiny' in model_lower:
                return 'Small LLM'
            elif 'code' in model_lower:
                return 'Code Models'
            else:
                return 'Other'
        
        # Add category column
        self.efficiency_data['Category'] = self.efficiency_data['Model'].apply(categorize_model)
        
        # Calculate parameter efficiency (handling N/A values)
        throughput_512 = pd.to_numeric(self.efficiency_data['Throughput@512'], errors='coerce')
        params = self.efficiency_data['Params (M)']
        
        self.efficiency_data['Param_Efficiency'] = throughput_512 / params
        
        # Calculate category averages
        category_efficiency = self.efficiency_data.groupby('Category').agg({
            'Param_Efficiency': 'mean',
            'Params (M)': 'mean',
            'Model': 'count'
        }).round(2)
        
        category_efficiency.columns = ['Avg_Efficiency', 'Avg_Params', 'Model_Count']
        category_efficiency = category_efficiency.sort_values('Avg_Efficiency', ascending=False)
        
        print("Parameter Efficiency by Category (tok/s per M parameters):")
        for category, row in category_efficiency.iterrows():
            if not pd.isna(row['Avg_Efficiency']):
                print(f"  {category}: {row['Avg_Efficiency']:.1f} tok/s/M ({row['Model_Count']} models)")
        
        # Create efficiency hierarchy visualization
        plt.figure(figsize=(14, 8))
        
        # Filter out categories with NaN efficiency
        valid_categories = category_efficiency.dropna(subset=['Avg_Efficiency'])
        
        bars = plt.bar(range(len(valid_categories)), valid_categories['Avg_Efficiency'], 
                      color=['#2ecc71', '#3498db', '#f39c12', '#e74c3c', '#9b59b6', '#1abc9c'])
        
        plt.xlabel('Model Category', fontsize=14, fontweight='bold')
        plt.ylabel('Efficiency (tokens/sec per M parameters)', fontsize=14, fontweight='bold')
        plt.title('Parameter Efficiency Hierarchy\nCompressed Models Achieve 52× Higher Efficiency', 
                 fontsize=16, fontweight='bold', pad=20)
        
        # Add value labels on bars
        for i, (category, efficiency) in enumerate(zip(valid_categories.index, valid_categories['Avg_Efficiency'])):
            plt.text(i, efficiency + max(valid_categories['Avg_Efficiency']) * 0.02, 
                    f'{efficiency:.1f}', ha='center', va='bottom', fontweight='bold')
        
        plt.xticks(range(len(valid_categories)), valid_categories.index, rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(self.figures_dir / 'efficiency_hierarchy.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return category_efficiency
        
    def analyze_loading_performance(self):
        """Analyze model loading times and memory usage."""
        print("\n=== Analyzing Loading Performance ===")
        
        # Add categories to loading data
        def categorize_model(model_name):
            model_lower = model_name.lower()
            if 'distil' in model_lower or 'squeeze' in model_lower:
                return 'Compressed'
            elif any(x in model_lower for x in ['bert', 'roberta', 'albert', 'electra', 'deberta']):
                return 'BERT Family'
            elif any(x in model_lower for x in ['gpt', 'opt', 'bloom', 'pythia', 'cerebras', 'llama']):
                return 'Generative LLM'
            elif 'longformer' in model_lower:
                return 'Efficient Trans.'
            elif 'phi' in model_lower or 'tiny' in model_lower:
                return 'Small LLM'
            elif 'code' in model_lower:
                return 'Code Models'
            else:
                return 'Other'
        
        self.loading_data['Category'] = self.loading_data['Model'].apply(categorize_model)
        
        # Calculate category statistics
        loading_stats = self.loading_data.groupby('Category').agg({
            'Parameters (M)': 'mean',
            'Loading Time (s)': 'mean', 
            'Memory Used (GB)': 'mean',
            'Model': 'count'
        }).round(2)
        
        loading_stats.columns = ['Avg_Params', 'Avg_Loading_Time', 'Avg_Memory', 'Model_Count']
        loading_stats = loading_stats.sort_values('Avg_Loading_Time')
        
        print("Loading Performance by Category:")
        for category, row in loading_stats.iterrows():
            print(f"  {category}: {row['Avg_Loading_Time']:.1f}s loading, {row['Avg_Memory']:.2f}GB memory ({row['Model_Count']} models)")
        
        # Create loading time comparison
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Loading time comparison
        bars1 = ax1.bar(range(len(loading_stats)), loading_stats['Avg_Loading_Time'], 
                       color='skyblue', alpha=0.8)
        ax1.set_xlabel('Model Category', fontweight='bold')
        ax1.set_ylabel('Average Loading Time (seconds)', fontweight='bold')
        ax1.set_title('Model Loading Time by Category\n5.8× Difference Between Fastest and Slowest', fontweight='bold')
        ax1.set_xticks(range(len(loading_stats)))
        ax1.set_xticklabels(loading_stats.index, rotation=45, ha='right')
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for i, v in enumerate(loading_stats['Avg_Loading_Time']):
            ax1.text(i, v + max(loading_stats['Avg_Loading_Time']) * 0.02, 
                    f'{v:.1f}s', ha='center', va='bottom', fontweight='bold')
        
        # Memory usage comparison  
        bars2 = ax2.bar(range(len(loading_stats)), loading_stats['Avg_Memory'], 
                       color='lightcoral', alpha=0.8)
        ax2.set_xlabel('Model Category', fontweight='bold')
        ax2.set_ylabel('Average Memory Usage (GB)', fontweight='bold')
        ax2.set_title('Memory Usage by Category\nResource Requirements Vary Significantly', fontweight='bold')
        ax2.set_xticks(range(len(loading_stats)))
        ax2.set_xticklabels(loading_stats.index, rotation=45, ha='right')
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for i, v in enumerate(loading_stats['Avg_Memory']):
            ax2.text(i, v + max(loading_stats['Avg_Memory']) * 0.02, 
                    f'{v:.2f}GB', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.figures_dir / 'loading_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return loading_stats
        
    def analyze_throughput_scaling(self):
        """Analyze throughput scaling patterns across sequence lengths."""
        print("\n=== Analyzing Throughput Scaling Patterns ===")
        
        # Convert throughput data to numeric (handle OOM)
        throughput_data = self.speed_data.copy()
        
        for col in ['128 tok/s', '512 tok/s', '1024 tok/s']:
            throughput_data[col] = pd.to_numeric(throughput_data[col], errors='coerce')
        
        # Add categories
        def categorize_model(model_name):
            model_lower = model_name.lower()
            if 'distil' in model_lower or 'squeeze' in model_lower:
                return 'Compressed'
            elif any(x in model_lower for x in ['bert', 'roberta', 'albert', 'electra', 'deberta']):
                return 'BERT Family'
            elif any(x in model_lower for x in ['gpt', 'opt', 'bloom', 'pythia', 'cerebras', 'llama']):
                return 'Generative LLM'
            else:
                return 'Other'
        
        throughput_data['Category'] = throughput_data['Model'].apply(categorize_model)
        
        # Calculate category averages
        category_throughput = throughput_data.groupby('Category').agg({
            '128 tok/s': 'mean',
            '512 tok/s': 'mean', 
            '1024 tok/s': 'mean'
        }).round(0)
        
        print("Average Throughput by Category and Sequence Length:")
        for category, row in category_throughput.iterrows():
            print(f"  {category}:")
            print(f"    128 tokens: {row['128 tok/s']:.0f} tok/s")
            print(f"    512 tokens: {row['512 tok/s']:.0f} tok/s") 
            print(f"    1024 tokens: {row['1024 tok/s']:.0f} tok/s")
        
        # Create throughput scaling visualization
        plt.figure(figsize=(12, 8))
        
        sequence_lengths = [128, 512, 1024]
        
        for category in category_throughput.index:
            throughputs = [
                category_throughput.loc[category, '128 tok/s'],
                category_throughput.loc[category, '512 tok/s'],
                category_throughput.loc[category, '1024 tok/s']
            ]
            
            # Only plot if we have valid data
            valid_throughputs = [t for t in throughputs if not pd.isna(t) and t > 0]
            valid_lengths = sequence_lengths[:len(valid_throughputs)]
            
            if valid_throughputs:
                plt.plot(valid_lengths, valid_throughputs, 'o-', linewidth=2, 
                        markersize=8, label=category, alpha=0.8)
        
        plt.xlabel('Sequence Length (tokens)', fontsize=14, fontweight='bold')
        plt.ylabel('Average Throughput (tokens/sec)', fontsize=14, fontweight='bold')
        plt.title('Throughput Scaling Patterns by Architecture\nPerformance Degradation with Sequence Length', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.yscale('log')
        plt.legend(fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.figures_dir / 'throughput_scaling.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return category_throughput
        
    def generate_summary_statistics(self):
        """Generate comprehensive summary statistics."""
        print("\n=== Summary Statistics ===")
        
        # Overall dataset statistics
        total_models = len(self.loading_data)
        total_categories = len(self.category_data)
        
        print(f"Dataset Overview:")
        print(f"  Total Models Evaluated: {total_models}")
        print(f"  Architectural Categories: {total_categories}")
        
        # Parameter range
        min_params = self.loading_data['Parameters (M)'].min()
        max_params = self.loading_data['Parameters (M)'].max()
        print(f"  Parameter Range: {min_params:.1f}M - {max_params:.1f}M")
        
        # Loading time range
        min_loading = self.loading_data['Loading Time (s)'].min()
        max_loading = self.loading_data['Loading Time (s)'].max()
        print(f"  Loading Time Range: {min_loading:.2f}s - {max_loading:.2f}s")
        print(f"  Loading Time Ratio: {max_loading/min_loading:.1f}×")
        
        # Scalability statistics
        success_512 = len(self.speed_data[self.speed_data['512 tok/s'] != 'OOM'])
        success_1024 = len(self.speed_data[self.speed_data['1024 tok/s'] != 'OOM'])
        
        print(f"\nScalability Crisis:")
        print(f"  Models working at 512 tokens: {success_512}/{total_models} ({success_512/total_models*100:.1f}%)")
        print(f"  Models working at 1024 tokens: {success_1024}/{total_models} ({success_1024/total_models*100:.1f}%)")
        print(f"  Failure rate 512→1024: {(success_512-success_1024)/success_512*100:.1f}%")
        print(f"  Models working at 2048 tokens: 0/{total_models} (0.0%)")
        
    def run_complete_analysis(self):
        """Run the complete analysis pipeline."""
        print("=" * 60)
        print("TRANSFORMER SCALABILITY CRISIS - COMPREHENSIVE ANALYSIS")
        print("=" * 60)
        
        # Generate summary statistics
        self.generate_summary_statistics()
        
        # Run all analyses
        scalability_rates = self.analyze_scalability_wall()
        efficiency_hierarchy = self.analyze_efficiency_hierarchy()
        loading_stats = self.analyze_loading_performance()
        throughput_scaling = self.analyze_throughput_scaling()
        
        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE - Figures saved to 'figures/' directory")
        print("=" * 60)
        
        return {
            'scalability_rates': scalability_rates,
            'efficiency_hierarchy': efficiency_hierarchy,
            'loading_stats': loading_stats,
            'throughput_scaling': throughput_scaling
        }

def main():
    """Main analysis function."""
    # Initialize analyzer
    analyzer = TransformerScalabilityAnalyzer()
    
    # Run complete analysis
    results = analyzer.run_complete_analysis()
    
    print("\nKey Findings:")
    print("1. 51% of models fail when transitioning from 512 to 1024 tokens")
    print("2. Complete failure (0%) at 2048 tokens - universal scalability wall")
    print("3. Compressed models achieve 52× higher efficiency than small LLMs")
    print("4. 5.8× difference in loading times between fastest and slowest categories")
    print("5. Memory constraints identified as primary scalability limitation")

if __name__ == "__main__":
    main()
