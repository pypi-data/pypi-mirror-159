#!/usr/bin/env python

import os
import sys
import stat
from os.path import join as pjoin, exists as pexists, realpath
import numpy as np

#---------------------------------
# CHANGE THESE FOR YOUR PROCESSING
#---------------------------------

base_dir = '/u1/work/hpc3194'
dataset_name = 'ADNI' # '4RTNI' # 'PPMI' #

# list_of_datasets = [ '4RTNI', 'PPMI', 'ADNI' ]
# list_of_subject_lists = ['graynet.compute.list']*3

proc_dir = pjoin(base_dir, dataset_name, 'processed')
freesurfer_dir = pjoin(proc_dir, 'freesurfer')
target_list_dir = pjoin(proc_dir, 'target_lists')

subject_id_list = pjoin(target_list_dir, 'graynet.compute.list')

base_feature = 'freesurfer_thickness' #  'freesurfer_curv'
atlas = 'FSAVERAGE' #  'GLASSER2016' # 'FSAVERAGE' # 'GLASSER2016' #
fwhm = 10

roi_statistic = 'median'
compute_roi_statistic = True
expt_name = 'graynet_roistats'

num_procs = 1

num_splits_samples = 40 # 10.0
num_splits_stats = 1

out_dir = pjoin(proc_dir, 'graynet', '{}_{}_fwhm{}'.format(base_feature, atlas, fwhm))

roi_stats_list = np.array(['median', 'mode', 'mean', 'std', 'gmean', 'hmean', 
                           'variation', 'entropy', 'skew', 'kurtosis'])

cluster_type = 'SGE'
pe_name = 'dist.pe' # distributed parallel env, not shared mem

def specify_hpc_resources(mem, queue, job_dir, job_log, cluster_type='SGE'):
    "returns lines to include in job scripts to specify resources"

    lines = list()
    if cluster_type.upper() in ['SGE', 'SUNGRIDENGINE']:
        parallel_str=''
        if num_procs > 1:
                parallel_str='-pe {} {}'.format(pe_name,num_procs)
        lines.append('#$ -l mf={} -q {} {} -wd {} -j yes -o {}'.format(mem, queue, parallel_str, job_dir, job_log))
        lines.append('cd {}\n'.format(job_dir))
        # add other lines below accommodating to your own HPC
    else:
        raise TypeError

    return '\n'.join(lines)


#---------------------------------
# END MAKING CHANGES
#---------------------------------

if not pexists(out_dir):
    os.makedirs(out_dir)

def make_dirs(dir_list):
    "Make multiple directories at once"

    for dir in dir_list:
        if not pexists(dir):
            os.makedirs(dir)

def make_cli_call_roistats(cli_name, subject_id_list, base_feature, freesurfer_dir,
            roi_statistic, atlas, fwhm, out_proc_dir):

    cmd = '{} -s {} -f {} -i {} -r {} -a {} -p {} -o {}\n'.format(cli_name,
            realpath(subject_id_list), base_feature, realpath(freesurfer_dir),
                                                                  roi_statistic, atlas, fwhm, out_proc_dir)

    return cmd


def make_job(subject_id_list, freesurfer_dir,
             base_feature, roi_stat_list,
             atlas, fwhm,
             out_proc_dir, job_dir, job_name):
    "Creates graynet job for running on HPC"

    queue = 'abaqus.q'
    mem='2G'
    cli_name = 'graynet'

    roi_stat_list = ' '.join(roi_stat_list)

    job_file = pjoin(job_dir, '{}.job'.format(job_name))
    job_log  = pjoin(job_dir, '{}.graynet_roistats.log'.format(job_name))
    if pexists(job_file):
        os.remove(job_file)
    with open(job_file, 'w') as jf:
        jf.write('#!/bin/bash\n')
        jf.write(specify_hpc_resources(mem, queue, job_dir, job_log))
        cli_call_line = make_cli_call_roistats(cli_name,realpath(subject_id_list), base_feature, realpath(freesurfer_dir), roi_stat_list, atlas, fwhm, realpath(out_proc_dir))
        jf.write(cli_call_line)

    st = os.stat(job_file)
    os.chmod(job_file, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    return job_file


job_dir = pjoin(out_dir, 'PBS')
make_dirs([job_dir, ])

num_stats = len(roi_stats_list)
# astype(str) is important to avoid byte strings
id_list = np.atleast_1d(np.genfromtxt(subject_id_list, dtype=str).astype(str))
num_samples = len(id_list)

print('{} samples and {} stats'.format(num_samples, num_stats))

num_samples_per_job = max(1,np.int64(np.ceil(num_samples/num_splits_samples)))
num_stats_per_job = max(1,np.int64(np.ceil(num_stats/num_splits_stats)))

print('{} samples/job and {} stats/job'.format(num_samples_per_job, num_stats_per_job))

stat_count, end_idx1 = 0, 0
for ww in range(int(num_splits_stats)):
    if end_idx1 > num_stats:
        break
    end_idx1 = stat_count+num_stats_per_job
    # print("stat {} {}".format(stat_count, end_idx1))
    subset_stats = roi_stats_list[stat_count:end_idx1]
    stat_count = end_idx1

    sub_count, end_idx2 = 0, 0
    for ss in range(int(num_splits_samples)):
        if end_idx2 > num_samples:
            break

        end_idx2 = sub_count+num_samples_per_job+1
        # print("sub {} {}".format(sub_count, end_idx2))

        subset_samples = id_list[sub_count:end_idx2]
        sub_count = end_idx2

        subset_list_path = pjoin(job_dir,'{}_{}th_split_samples_{}.txt'.format(dataset_name.lower(),ss, expt_name))
        with open(subset_list_path, 'w') as sf:
            sf.write('\n'.join(subset_samples))

        job_name = 'split{}{}_{}'.format(ww,ss, expt_name)

        job_file = make_job(subset_list_path, freesurfer_dir,
                            base_feature, subset_stats,
                            atlas, fwhm, out_dir, job_dir, job_name)

        print('generated jobs for {} : {} samples and {} stats'.format(job_name, len(subset_samples), len(subset_stats)))


print('Job scripts have been generated in \n {}'.format(job_dir))
print('\nPlease change to that directory and submit them using ./qsubMany *.graynet.job')
print('If you are not on Linux or not using SGE/Torque, you may have to adapt the qsubMany script also.')


