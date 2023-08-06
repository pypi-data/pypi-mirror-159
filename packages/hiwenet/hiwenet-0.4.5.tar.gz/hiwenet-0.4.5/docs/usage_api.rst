------------------
Examples using API
------------------

This package computes single-subject networks, hence you may need loop over samples/subjects in your dataset to extract them for all the samples/subjects.
Them proceed to your typical subsequent analysis (such as classification etc).

Note: 

 - The `hiwenet.extract` could be used to extract advance covariance/connectome features in place of `MNE.extract_label_time_course <http://martinos.org/mne/stable/generated/mne.SourceEstimate.html#mne.SourceEstimate.extract_label_time_course>`_ or nilearn.input_data.NiftiLabelsMasker.transform - see `here <http://nilearn.github.io/connectivity/functional_connectomes.html#extracting-signals-on-a-parcellation>`_ and `here <http://nilearn.github.io/modules/generated/nilearn.input_data.NiftiLabelsMasker.html#nilearn.input_data.NiftiLabelsMasker.transform>`_. 
 - However, we plan to add interfaces to tools e.g. via a scikit-learn compatible API/interface is also in the works. Stay tuned.

A rough example of usage when using the hiwenet API can be:

.. TODO add examples to show how hiwenet can be used in place of ConnectomeMeasure of nilearn, or other uses in MNE.


.. code-block:: python

    import hiwenet
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    import numpy as np
    import nibabel
    import os

    # ------------------------------------------------------------------------------------
    # see docs/example_thickness_hiwenet.py for a concrete example
    # ------------------------------------------------------------------------------------

    for ss, subject in enumerate(subject_list):
      features = get_features(subject)
      edge_weight_matrix = hiwenet.extract(features, groups,  weight_method = 'kullback_leibler')
      edge_weights_vec[ss,:] = upper_tri_vec(edge_weight_matrix)

      out_file = os.path.join(out_folder, 'hiwenet_{}.txt'.format(subject))
      np.save(out_file, edge_weight_matrix)


    # proceed to analysis


    # very rough example for training/evaluating a classifier
    rf = RandomForestClassifier(oob_score = True)
    scores = cross_val_score(rf, edge_weights_vec, subject_labels)



A fuller example (still a bit rough) for cortical thickness applications can be shown below:

.. code-block:: python

    #~/usr/bin/env python

    import hiwenet
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    import numpy as np
    import nibabel
    import os

    # ----------------------------------------------------
    # toy examples - modify for your application/need
    my_project = '/data/myproject'
    subject_list = ['a1', 'b2', 'c3', 'd4']
    subject_labels = [1, 1, -1, -1]

    num_subjects = len(subject_list)
    # number of features (imaging vertex-wise cortical thickness values over the whole brain)
    feature_dimensionality = 1000
    num_ROIs = 50
    edge_weights = np.empty(num_subjects, num_ROIs*(num_ROIs-1)/2.0)

    atlas = 'fsaverage'
    # ----------------------------------------------------

    def get_parcellation(atlas, parcel_param):
        "Placeholder to insert your own function to return parcellation in reference space."

        parc_path = os.path.join(atlas, 'parcellation_param{}.mgh'.format(parcel_param))
        parcel = nibabel.freesurfer.io.read_geometry(parc_path)

        return parcel


    groups = get_parcellation(atlas, feature_dimensionality)

    out_folder = os.path.join(my_project, 'hiwenet')

    # choose a method from one from among the three groups (metrics, semi-metrics and similarity functions)
    metrics = [ 'manhattan', 'minowski', 'euclidean', 'noelle_2', 'noelle_4', 'noelle_5' ]

    semi_metric_list = [
        'kullback_leibler', 'cosine_1',
        'jensen_shannon', 'chi_square',
        'chebyshev', 'chebyshev_neg',
        'histogram_intersection_1',
        'relative_deviation', 'relative_bin_deviation',
        'noelle_1', 'noelle_3',
        'correlate_1']
    similarity_func = ['correlate', 'cosine', 'cosine_2', 'cosine_alt', 'fidelity_based']


    def get_features(subject_id):
        "Placeholder to insert your own function to read subject-wise features."

        features_path = os.path.join(my_project,'base_features', subject_id, 'features.txt')
        feature_vector = np.loadtxt(features_path)

        return feature_vector


    def upper_tri_vec(matrix):
        "Returns the vectorized values of upper triangular part of a matrix"

        triu_idx = np.triu_indices_from(matrix, 1)
        return matrix[triu_idx]

    num_links = num_ROIs*(num_ROIs-1)/2.0
    edge_weights_vec = np.zeros(len(subject_list), num_links)
    for ss, subject in enumerate(subject_list):
      features = get_features(subject)
      edge_weight_matrix = hiwenet.extract(features, groups,  weight_method = 'kullback_leibler')
      edge_weights_vec[ss,:] = upper_tri_vec(edge_weight_matrix)

      out_file = os.path.join(out_folder, 'hiwenet_{}.txt'.format(subject))
      np.save(out_file, edge_weight_matrix)


    # proceed to analysis

    # very rough example for training/evaluating a classifier
    rf = RandomForestClassifier(oob_score = True)
    scores = cross_val_score(rf, edge_weights_vec, subject_labels)

