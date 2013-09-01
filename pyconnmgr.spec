# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           pyconnmgr
Version:        4.0.0
Release:        4%{?dist}
Summary:        Simple Python/Glade frontend to SSH, VNC and rdesktop commands.
Group:          Applications/Internet

License:        GPL v2
URL:            http://www.thelupine.com/pyconnmgr
Source0:        pyconnmgr-4.0.0.tar.gz

BuildArch:      noarch
BuildRequires:  sqlite, pexpect, tigervnc, gnome-terminal, rdesktop

%description
pyconnmgr is a simple Python/Glade frontend to SSH, VNC and rdesktop commands. \
It was created as a learning process for developing in Python and Glade. Even though this was \
created as a learning process, the application itself turned out to be very useful.


%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%defattr(-,root,root,-)
/usr/bin/pyconnmgr
/usr/share/applications/pyconnmgr.desktop
/usr/share/pyconnmgr/pyconnmgr-gtk2.glade
/usr/share/pyconnmgr/pyconnmgr-gtk3.glade
/usr/share/pyconnmgr/pyconnmgr.glade
/usr/share/pyconnmgr/pyconnmgr.png
/usr/share/pyconnmgr/pyconnmgr32x32.png
/usr/share/pyconnmgr/pyconnmgr64x64.png
%doc
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Sat Aug 31 2013 TheLupine <thelupine@gmail.com> - 4.0.0
- new Fedora build - using TigerVNC
