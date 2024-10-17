%global packname  robust
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4.15
Release:          1
Summary:          Robust Library
Group:            Sciences/Mathematics
License:          GPLv1+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-15.tar.gz

Requires:         R-fit.models R-MASS R-lattice R-robustbase R-rrcov 
Requires:         R-stats R-robustbase 

BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-fit.models R-MASS R-lattice R-robustbase R-rrcov
BuildRequires:    R-stats R-robustbase 

%description
A package of robust methods.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
