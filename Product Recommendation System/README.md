# Product Recommendation System

## Introduction
This document outlines the requirements for building a **product recommendation system** using the provided Amazon dataset. The goal is to leverage **user reviews, ratings, and product metadata** to create a **personalized recommendation system**.

## Dataset Overview
The dataset contains **1,465 records** and **16 columns**, with the following key features relevant to the recommendation system:

- **Product Details**: `product_id`, `product_name`, `category`, `discounted_price`, `actual_price`, `rating`
- **User Details**: `user_id`, `user_name`
- **User Feedback**: `review_id`, `review_title`, `review_content`, `rating`

## Project Objectives
1. Build a **personalized product recommendation system**.
2. Utilize **user reviews and ratings** to identify user preferences.
3. Recommend products based on **user behavior and product similarity**.

## Recommendation Approaches
The following techniques will be used:

1. **Collaborative Filtering**: Recommending products based on user-item interaction data.
2. **Content-Based Filtering**: Using product metadata (e.g., category, price, and reviews) to recommend similar products.
3. **Hybrid Methods**: Combining **collaborative and content-based** approaches for improved accuracy.



