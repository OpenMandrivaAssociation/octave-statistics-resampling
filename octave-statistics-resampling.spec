%global octpkg statistics-resampling

Summary:	Estimate bias, uncertainty (standard errors and confidence intervals) and test 
Name:		octave-statistics-resampling
Version:	5.6.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/statistics-resampling/
Url:		https://github.com/gnu-octave/statistics-resampling/
Source0:	https://github.com/gnu-octave/statistics-resampling/archive/refs/tags/%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Estimate bias, uncertainty (standard errors and confidence intervals) 
and test hypotheses (p-values) using resampling methods. (Note that 
versions of this package <= 5.4.3 are named statistics-bootstrap).

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

