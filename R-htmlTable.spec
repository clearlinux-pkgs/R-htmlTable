#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-htmlTable
Version  : 1.11.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/htmlTable_1.11.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/htmlTable_1.11.2.tar.gz
Summary  : Advanced Tables for Markdown/HTML
Group    : Development/Tools
License  : GPL-3.0
Requires: R-XML
Requires: R-checkmate
Requires: R-chron
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-lubridate
Requires: R-pxweb
Requires: R-reshape
Requires: R-rstudioapi
BuildRequires : R-XML
BuildRequires : R-checkmate
BuildRequires : R-chron
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-lubridate
BuildRequires : R-pxweb
BuildRequires : R-reshape
BuildRequires : R-rstudioapi
BuildRequires : clr-R-helpers

%description
column spanners, table spanners, zebra striping, and more. While allowing
    advanced layout, the underlying css-structure is simple in order to maximize
    compatibility with word processors such as 'MS Word' or 'LibreOffice'. The package
    also contains a few text formatting functions that help outputting text
    compatible with HTML/'LaTeX'.

%prep
%setup -q -c -n htmlTable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521179868

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521179868
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmlTable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmlTable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmlTable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library htmlTable|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/htmlTable/DESCRIPTION
/usr/lib64/R/library/htmlTable/INDEX
/usr/lib64/R/library/htmlTable/Meta/Rd.rds
/usr/lib64/R/library/htmlTable/Meta/data.rds
/usr/lib64/R/library/htmlTable/Meta/features.rds
/usr/lib64/R/library/htmlTable/Meta/hsearch.rds
/usr/lib64/R/library/htmlTable/Meta/links.rds
/usr/lib64/R/library/htmlTable/Meta/nsInfo.rds
/usr/lib64/R/library/htmlTable/Meta/package.rds
/usr/lib64/R/library/htmlTable/Meta/vignette.rds
/usr/lib64/R/library/htmlTable/NAMESPACE
/usr/lib64/R/library/htmlTable/NEWS
/usr/lib64/R/library/htmlTable/R/htmlTable
/usr/lib64/R/library/htmlTable/R/htmlTable.rdb
/usr/lib64/R/library/htmlTable/R/htmlTable.rdx
/usr/lib64/R/library/htmlTable/data/SCB.rda
/usr/lib64/R/library/htmlTable/doc/general.R
/usr/lib64/R/library/htmlTable/doc/general.Rmd
/usr/lib64/R/library/htmlTable/doc/general.html
/usr/lib64/R/library/htmlTable/doc/index.html
/usr/lib64/R/library/htmlTable/doc/tables.R
/usr/lib64/R/library/htmlTable/doc/tables.Rmd
/usr/lib64/R/library/htmlTable/doc/tables.html
/usr/lib64/R/library/htmlTable/doc/tidyHtmlTable.R
/usr/lib64/R/library/htmlTable/doc/tidyHtmlTable.Rmd
/usr/lib64/R/library/htmlTable/doc/tidyHtmlTable.html
/usr/lib64/R/library/htmlTable/examples/data-SCB_example.R
/usr/lib64/R/library/htmlTable/examples/htmlTable_example.R
/usr/lib64/R/library/htmlTable/examples/interactiveTable_example.R
/usr/lib64/R/library/htmlTable/help/AnIndex
/usr/lib64/R/library/htmlTable/help/aliases.rds
/usr/lib64/R/library/htmlTable/help/htmlTable.rdb
/usr/lib64/R/library/htmlTable/help/htmlTable.rdx
/usr/lib64/R/library/htmlTable/help/paths.rds
/usr/lib64/R/library/htmlTable/html/00Index.html
/usr/lib64/R/library/htmlTable/html/R.css
/usr/lib64/R/library/htmlTable/html_components/button.html
/usr/lib64/R/library/htmlTable/htmlwidgets/htmlTableWidget.js
/usr/lib64/R/library/htmlTable/htmlwidgets/htmlTableWidget.yaml
/usr/lib64/R/library/htmlTable/htmlwidgets/lib/jquery/jquery-AUTHORS.txt
/usr/lib64/R/library/htmlTable/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/htmlTable/htmlwidgets/lib/table_pagination/table_pagination.css
/usr/lib64/R/library/htmlTable/htmlwidgets/lib/table_pagination/table_pagination.js
/usr/lib64/R/library/htmlTable/javascript/button.js
/usr/lib64/R/library/htmlTable/javascript/toggler.js
