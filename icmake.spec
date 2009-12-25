Summary:        A hybrid between a 'make' utility and a 'shell script' language
Name:		icmake
Version:	7.12.5
Release:	%mkrel 1
License:	GPLv3
Group:		Development/Other
URL:		http://icmake.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
./icm_bootstrap /

%install
rm -rf %{buildroot}
./icm_install strip progs %{buildroot}
./icm_install scripts %{buildroot}
./icm_install skel %{buildroot}
./icm_install man %{buildroot}
./icm_install doc %{buildroot}
./icm_install docdoc %{buildroot}
./icm_install etc %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/ic*
%{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_docdir}/%{name}

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-doc
