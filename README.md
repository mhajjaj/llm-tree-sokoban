# Tree-Based Planning with LLMs for Sokoban

This project implements a tree-based planning system for solving Sokoban puzzles using a Large Language Model (LLM) as a **single-step action predictor**.

## Objectives
- Parse Sokoban puzzles from the Microban dataset
- Use an LLM to predict one action at a time
- Integrate predictions into a tree-search planner
- Evaluate performance across puzzle difficulty

## Constraints
- The LLM is used **only for single-step action prediction**
- Tree search handles long-horizon planning

## Dataset
Microban Sokoban puzzles by David W. Skinner.

## Structure
- `sokoban/env`: Sokoban parser and simulator
- `sokoban/llm`: LLM action predictor
- `sokoban/search`: Tree search algorithms
- `evaluation`: Metrics and analysis
- `experiments`: Experimental configurations

## Status
Initial setup
