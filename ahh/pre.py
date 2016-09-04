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
    :param: dir (str) - name of directory for files to be saved
    """
    fi_dir = os.path.join(base_url, glob_str)
    if user is not None and pwd is not None:
        wget_cmd =\
                  "wget -r -np -nd --glob=on --user={user} \
                  --password={pwd} '{fi_dir}'"\
                  .format(user=user, pwd=pwd, fi_dir=fi_dir)
    else:
        wget_cmd = """wget -r -np -nd --glob=on '{fi_dir}'""" \
            .format(fi_dir=fi_dir)
    if directory is not None:
        add_on_cmd = """ -P {}""".format(directory)
        wget_cmd += add_on_cmd
    os.system(wget_cmd)


def concat_nc(glob_str, output_fi, append_rec_dim=None):
    """
    Wrapper of NCO's ncrcat and optional ncks; concatenates a list of netCDF
    files given a glob_str (i.e. 'THETA.1440x720x50.2010*.nc') and outputs
    concatenated file as the given output_fi. If there's an error complaining
    that there's no record dimension, can give the dimension name to
    concatenate across under append_rec_dim.

    :param: glob_str (str) - the naming pattern of the files
    :param: output_fi (str) - name of concatenated file
    :param: append_rec_dim (str) - name of dimension to act as record dimension
    """
    url_names = sorted(glob.glob('{}'.format(glob_str)))

    if append_rec_dim is not None:
        rec_append_cmd = \
            'ncks -O --mk_rec_dmn {append_rec_dim} {fi_name} RD.{fi_name}' \
            .format(append_rec_dim=append_rec_dim, fi_name=url_names[0])
        os.system(rec_append_cmd)
        rec_str = 'RD.{fi_name}'.format(fi_name=url_names[0])
        url_list = [rec_str] + url_names[1:]
    else:
        url_list = url_names

    url_list_str = ' '.join(url_list)
    os.system('ncrcat {input_list} {output_fi}'.format(
        input_list=url_list_str, output_fi=output_fi))
