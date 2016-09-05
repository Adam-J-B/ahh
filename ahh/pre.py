import glob
import os

__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'


def wget_fi(base_url, glob_str, user=None, pwd=None, directory=None):
    """
    Wrapper of wget; downloads files that matches the given glob_str. Can input
    username and password if authentication is required.

    :param: base_url (str) - the dir of all the to be downloaded files
    :param: glob_str (str) - the naming pattern of the files
    :param: user (str) - username
    :param: pwd (str) - password
    :param: directory (str) - name of directory for files to be saved
    """
    fi_dir = os.path.join(base_url, glob_str)
    if user is not None and pwd is not None:
        wget_cmd =\
                  "wget -r -np -nd -nc --glob=on --user={user} \
                  --password={pwd} '{fi_dir}'"\
                  .format(user=user, pwd=pwd, fi_dir=fi_dir)
    else:
        wget_cmd = """wget -r -np -nd -nc --glob=on '{fi_dir}'""" \
            .format(fi_dir=fi_dir)
    if directory is not None:
        add_on_cmd = """ -P {}""".format(directory)
        wget_cmd += add_on_cmd
    os.system(wget_cmd)


def ncdump(glob_str, directory='./'):
    """
    Wrapper of ncdump; prints out netCDF metadata.

    :param: glob_str (str) - the naming pattern of the files
    :param: directory (str) - directory of file
    """
    fi_dir = os.path.join(directory, glob_str)
    try:
        fi_in_str = sorted(glob.glob('{}'.format(fi_dir)))[0]
        ncdump_cmd = 'ncdump -h {}'.format(fi_in_str)
        os.system(ncdump_cmd)
    except:
        print('Could not ncdump file!')


def concat_nc(glob_str, output_fi, directory='./', rec_dim=None):
    """
    Wrapper of NCO's ncrcat and optional ncks; concatenates a list of netCDF
    files given a glob_str (i.e. 'THETA.1440x720x50.2010*.nc') and outputs
    concatenated file as the given output_fi. If there's an error complaining
    that there's no record dimension, can give the dimension name to
    concatenate across under rec_dim.

    :param: glob_str (str) - the naming pattern of the files
    :param: output_fi (str) - name of concatenated file
    :param: directory (str) - directory of both input and output files
    :param: rec_dim (str) - name of dimension to act as record dimension
    """
    fi_dir = os.path.join(directory, glob_str)
    final_output = os.path.join(directory, output_fi)
    url_names = sorted(glob.glob('{}'.format(fi_dir)))
    fi_name = url_names[0]

    if rec_dim is not None:
        if os.path.isfile('{}_rd'.format(fi_name)):
            print('{fi_name}_rd already exists! Not remaking {fi_name}_rd.'
                  .format(fi_name=fi_name))
        else:
            rec_append_cmd = \
                'ncks -O --mk_rec_dmn {rec_dim} {fi_name} {fi_name}_rd' \
                .format(rec_dim=rec_dim, fi_name=fi_name)
            os.system(rec_append_cmd)
        rec_str = '{}_rd'.format(fi_name)
        url_list = [rec_str] + url_names[1:]
    else:
        url_list = url_names

    url_list_str = ' '.join(url_list)
    os.system('ncrcat {input_list} {output_fi}'.format(
        input_list=url_list_str, output_fi=final_output))
