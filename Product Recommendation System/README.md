Introduction
This document outlines the requirements for building a product recommendation system using the provided Amazon dataset. The goal is to leverage user reviews, ratings, and product metadata to create a personalized recommendation system.
Dataset Overview
The dataset contains 1,465 records and 16 columns, with the following key features relevant for a recommendation system:
•	1. Product Details: product_id, product_name, category, discounted_price, actual_price, rating.
•	2. User Details: user_id, user_name.
•	3. User Feedback: review_id, review_title, review_content, rating.
Project Objectives
1. To build a personalized product recommendation system.
2. To utilize user reviews and ratings to identify user preferences.
3. To recommend products based on user behavior and product similarity.
Recommendation Approaches
The following approaches will be considered for the recommendation system:

•	1. Collaborative Filtering: Leveraging user-item interaction data to recommend products.
•	2. Content-Based Filtering: Using product metadata such as category, price, and reviews to recommend similar products.
•	3. Hybrid Methods: Combining collaborative and content-based approaches for improved accuracy.

