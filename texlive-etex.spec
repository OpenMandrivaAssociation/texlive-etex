%global tl_name etex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An extended version of TeX, from the NTS project
Group:		Publishing
URL:		https://www.ctan.org/pkg/etex
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extended version of TeX (capable of running as if it were unmodified
TeX). E-TeX has been specified by the LaTeX team as the base engine for
LaTeX2e. Thus, LaTeX programmers may assume e-TeX functionality, along
with additional extensions. The pdftex engine and others directly
incorporate the e-TeX extensions. The etex program in most distributions
is an incarnation of pdftex running in DVI mode. The development source
for e-TeX is the TeX Live source repository, although further extensions
have taken place in the pdftex and other engine sources, keeping e-TeX
stable.

