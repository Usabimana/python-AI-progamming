#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:USABIMANA Pascal
# DATE CREATED: 29 December 2019                                  
# REVISED DATE: 07 January 2019
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    
#-------------------------------------------------------------------------------------------------------------------------------------------
    # initialisations
    results_stats_dic = dict()  # Create an empty dictionary
    
    # initialise initial dictionary keys values
    results_stats_dic['n_images'] = 0 # number of images
    results_stats_dic['n_dogs_img'] = 0 # number of dog images
    results_stats_dic['n_notdogs_img'] =0 # number of NON-dog images
    results_stats_dic['n_match'] = 0 # number of matches between pet & classifier labels
    results_stats_dic['n_correct_dogs'] = 0 # number of correctly classified dog images
    results_stats_dic['n_correct_notdogs'] = 0 # number of correctly classified NON-dog images
    results_stats_dic['n_correct_breed'] = 0 # number of correctly classified dog breeds
    results_stats_dic['pct_match'] = 0 # percentage of correct matches
    results_stats_dic['pct_correct_dogs'] = 0 # percentage of correctly classified dogs
    results_stats_dic['pct_correct_breed'] = 0 # percentage of correctly classified dog breeds
    results_stats_dic['pct_correct_notdogs'] = 0 # percentage of correctly classified NON-dogs
    
#-------------------------------------------------------------------------------------------------------------------------------------------
    # number of images in images dictionary
    results_stats_dic['n_images'] = len(results_dic) # number of images
    
#-------------------------------------------------------------------------------------------------------------------------------------------   
    for key in results_dic:
        #------------------------------------------------------------------------------------------------------ 
        #count the correct breed and count number of matches
        if results_dic[key][2] == 1 and results_dic[key][3] == 1: #pet image is a dogbut from pet and class label img match 
            results_stats_dic['n_correct_breed'] += 1      # number of correct breed dogs
            
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1 # counts number of matches between pet & classifier labels
            
        #-----------------------------------------------------------------------------------------------
        # counts is a dogs and is not dogs
        if results_dic[key][3] == 1: #pet images is as dog
            results_stats_dic['n_dogs_img'] += 1  # number pets is a dogs
            
        if results_dic[key][3] == 0: #classified image as Dog (& pet image is a dog)
            results_stats_dic['n_notdogs_img'] += 1 # number of not dogs
            
        #----------------------------------------------------------------------------------------------        
        #counts the classified as corrected dogs and not dogs
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            results_stats_dic['n_correct_dogs'] += 1 # Number of Correct dogs
            
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            #  pet image isn't a dog
            results_stats_dic['n_correct_notdogs'] += 1 # counts number of correct NOT dog clasifications.
  

#--------------------------------------------------------------------------------------------------------------------------------------------
    # Calculates the percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match']/results_stats_dic['n_images']) * 100 # percentage of all matches labels from all images
    
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img'])*100.0 # percentage of correct dogs from all dogs
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img'])*100.0 #percentage of not correct dogs from notdogs
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] =(results_stats_dic['n_correct_breed']/results_stats_dic['n_dogs_img']) * 100 # percentage of correct breed from all dogs
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

#---------------------------------------------------------------------------------------------------------------------------------------------
    

    return results_stats_dic
