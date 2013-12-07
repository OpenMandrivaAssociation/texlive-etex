# revision 31600
# category Package
# catalog-ctan /systems/e-tex
# catalog-date 2012-03-09 15:12:11 +0100
# catalog-license knuth
# catalog-version 2.1
Name:		texlive-etex
Version:	2.1
Release:	4
Summary:	An extended version of TeX, from the NTS project
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/e-tex
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An extended version of TeX (which is capable of running as if
it were TeX unmodified). E-TeX has been specified by the LaTeX
team as the engine for the development of LaTeX 2e, in the
immediate future; as a result, LaTeX programmers may (in all
current TeX distributions) assume e-TeX functionality.
Development versions of e-TeX are to be found in the TeX live
source repository.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/etex/xbmc10.mf
%{_texmfdistdir}/fonts/tfm/public/etex/xbmc10.tfm
%{_texmfdistdir}/tex/plain/etex/etex.src
%{_texmfdistdir}/tex/plain/etex/etexdefs.lib
%doc %{_texmfdistdir}/doc/etex/base/NTS-FAQ
%doc %{_texmfdistdir}/doc/etex/base/etex_gen.tex
%doc %{_texmfdistdir}/doc/etex/base/etex_man.pdf
%doc %{_texmfdistdir}/doc/etex/base/etex_man.sty
%doc %{_texmfdistdir}/doc/etex/base/etex_man.tex
%doc %{_texmfdistdir}/doc/etex/base/etex_ref.html
%doc %{_texmfdistdir}/doc/etex/base/etex_src.html
%doc %{_texmfdistdir}/doc/etex/base/legal.html
%doc %{_texmfdistdir}/doc/etex/base/nts-group.html
%doc %{_texmfdistdir}/doc/etex/base/webmerge.tex
%doc %{_mandir}/man1/etex.1*
%doc %{_texmfdistdir}/doc/man/man1/etex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
