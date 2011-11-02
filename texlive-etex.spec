Name:		texlive-etex
Version:	2.1
Release:	1
Summary:	An extended version of TeX, from the NTS project
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/e-tex
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An extended version of TeX (which is capable of running as if
it were TeX unmodified). E-TeX has been specified by the LaTeX
team as the engine for the development of LaTeX, in the
immediate future; as a result, LaTeX programmers may (in all
current TeX distributions) assume e-TeX functionality.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
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
%doc %{_texmfdir}/doc/man/man1/etex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
