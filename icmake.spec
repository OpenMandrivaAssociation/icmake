%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A hybrid between a 'make' utility and a 'shell script' language
Name:		icmake
Version:	9.02.08
Release:	2
License:	GPLv3
Group:		Development/Other
Url:		https://fbb-git.github.io/icmake/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2

%description
Icmake is a hybrid between a 'make' utility and a 'shell script' language. 
Originally, it was written to provide a useful tool for automatic program 
maintenance and system administrative tasks on old MS-DOS platforms.

%package	doc
Group:		Development/Other
Summary:	Documentation for icmake

%description	doc
This package contains the documentation for icmake.

%prep
%setup -q

# set the correct LIBDIR path
sed -i -e "s:usr/lib:usr/%{_lib}:g" %{name}/INSTALL.im

# fix executable perms in examples
cd %{name}/examples
for i in am bup defines ds ftpxfer idir \
    initialization keep killprog nesteddirectives r tolower
do
    chmod -x $i
done
cd -

%build
%setup_compile_flags
export CFLAGS="%{optflags}"
cd %{name}
./icm_prepare /
./icm_bootstrap /
cd -

%install
cd %{name}
./icm_install progs %{buildroot}
./icm_install scripts %{buildroot}
./icm_install skel %{buildroot}
./icm_install man %{buildroot}
./icm_install doc %{buildroot}
./icm_install docdoc %{buildroot}
./icm_install etc %{buildroot}
cd -

%files
%{_bindir}/ic*
%{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_docdir}/%{name}

%files doc
%{_docdir}/%{name}-doc

