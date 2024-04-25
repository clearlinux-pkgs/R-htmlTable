#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-htmlTable
Version  : 2.4.2
Release  : 69
URL      : https://cran.r-project.org/src/contrib/htmlTable_2.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/htmlTable_2.4.2.tar.gz
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
BuildRequires : R-checkmate
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-rstudioapi
BuildRequires : R-stringr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
column spanners, table spanners, zebra striping, and more. While allowing
    advanced layout, the underlying css-structure is simple in order to maximize
    compatibility with common word processors. The package also contains a few
    text formatting functions that help outputting text compatible with HTML/LaTeX.

%prep
%setup -q -n htmlTable
pushd ..
cp -a htmlTable buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698684778

%install
export SOURCE_DATE_EPOCH=1698684778
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/htmlTable/NEWS.md
/usr/lib64/R/library/htmlTable/R/htmlTable
/usr/lib64/R/library/htmlTable/R/htmlTable.rdb
/usr/lib64/R/library/htmlTable/R/htmlTable.rdx
/usr/lib64/R/library/htmlTable/data/SCB.rda
/usr/lib64/R/library/htmlTable/doc/complex_tables.R
/usr/lib64/R/library/htmlTable/doc/complex_tables.Rmd
/usr/lib64/R/library/htmlTable/doc/complex_tables.html
/usr/lib64/R/library/htmlTable/doc/general.R
/usr/lib64/R/library/htmlTable/doc/general.Rmd
/usr/lib64/R/library/htmlTable/doc/general.html
/usr/lib64/R/library/htmlTable/doc/index.html
/usr/lib64/R/library/htmlTable/doc/text_formatters.R
/usr/lib64/R/library/htmlTable/doc/text_formatters.Rmd
/usr/lib64/R/library/htmlTable/doc/text_formatters.html
/usr/lib64/R/library/htmlTable/doc/tidyHtmlTable.R
/usr/lib64/R/library/htmlTable/doc/tidyHtmlTable.Rmd
/usr/lib64/R/library/htmlTable/doc/tidyHtmlTable.html
/usr/lib64/R/library/htmlTable/examples/concatHtmlTables_example.R
/usr/lib64/R/library/htmlTable/examples/data-SCB_example.R
/usr/lib64/R/library/htmlTable/examples/htmlTable_example.R
/usr/lib64/R/library/htmlTable/examples/interactiveTable_example.R
/usr/lib64/R/library/htmlTable/examples/tidyHtmlTable_example.R
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
/usr/lib64/R/library/htmlTable/tests/testthat/htmlTable_addHtmlTableStyle.R
/usr/lib64/R/library/htmlTable/tests/testthat/structure.tex
/usr/lib64/R/library/htmlTable/tests/testthat/ters-htmlTable_cell_styles_via_prPrepareCSS.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable-dimnames.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable-input_checks.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_cgroup.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_dates.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_escape_html.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_rgroup_tspanner.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_styles.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-htmlTable_total.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-interactiveTable.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-theming.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-tidyHtmlTable.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-tidyHtmlTable_Hmisc_latex.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-tidyHtmlTable_sorting.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-txtFrmt.R
/usr/lib64/R/library/htmlTable/tests/testthat/test-txtMergeLines.R
/usr/lib64/R/library/htmlTable/tests/visual_tests/htmlTable_vtests.R
/usr/lib64/R/library/htmlTable/tests/visual_tests/pandoc_test.Rmd
/usr/lib64/R/library/htmlTable/tests/visual_tests/word_test.Rmd
/usr/lib64/R/library/htmlTable/tests/visual_tests/word_test.html
