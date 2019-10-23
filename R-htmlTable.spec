#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-htmlTable
Version  : 1.13.2
Release  : 33
URL      : https://cran.r-project.org/src/contrib/htmlTable_1.13.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/htmlTable_1.13.2.tar.gz
Summary  : Advanced Tables for Markdown/HTML
Group    : Development/Tools
License  : GPL-3.0
Requires: R-checkmate
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-knitr
Requires: R-magrittr
Requires: R-rstudioapi
Requires: R-stringr
BuildRequires : R-XML
BuildRequires : R-checkmate
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-plyr
BuildRequires : R-reshape
BuildRequires : R-rstudioapi
BuildRequires : R-stringr
BuildRequires : R-tidyr
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
[![Build Status](https://travis-ci.org/gforge/htmlTable.svg?branch=master)](https://travis-ci.org/gforge/htmlTable)
[![](https://cranlogs.r-pkg.org/badges/htmlTable)](https://cran.r-project.org/package=htmlTable)

%prep
%setup -q -c -n htmlTable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571843556

%install
export SOURCE_DATE_EPOCH=1571843556
rm -rf %{buildroot}
export LANG=C.UTF-8
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc htmlTable || :


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
/usr/lib64/R/library/htmlTable/tests/testInteractive.R
/usr/lib64/R/library/htmlTable/tests/testthat.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable-dimnames.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable-input_checks.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_cgroup.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_dates.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_rgroup_tspanner.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_styles.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_total.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-interactiveTable.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-txtFrmt.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-txtMergeLines.R
/usr/lib64/R/library/htmlTable/tests/visual_tests/htmlTable_vtests.R
/usr/lib64/R/library/htmlTable/tests/visual_tests/pandoc_test.Rmd
/usr/lib64/R/library/htmlTable/tests/visual_tests/word_test.Rmd
