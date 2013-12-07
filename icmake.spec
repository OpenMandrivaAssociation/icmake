%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:        A hybrid between a 'make' utility and a 'shell script' language
Name:		icmake
Version:	7.21.00
Release:	5
License:	GPLv3
Group:		Development/Other
Url:		http://icmake.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_%{version}.orig.tar.gz

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
sed -i -e "s:usr/lib:usr/%{_lib}:g" INSTALL.im

# fix executable perms in examples
pushd examples
for i in am backup bup defines ds ftpxfer idir \
	initialization keep killprog nesteddirectives r tolower
do
	chmod -x $i
done
popd

%build
%setup_compile_flags
./icm_bootstrap /

%install
./icm_install strip progs %{buildroot}
./icm_install scripts %{buildroot}
./icm_install skel %{buildroot}
./icm_install man %{buildroot}
./icm_install doc %{buildroot}
./icm_install docdoc %{buildroot}
./icm_install etc %{buildroot}

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

