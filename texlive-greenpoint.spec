%global tl_name greenpoint
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The Green Point logo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greenpoint
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Metafont-implementation of the logo commonly known as 'Der Grune
Punkt' ('The Green Point'). In Austria, it can be found on nearly every
bottle. It should not be confused with the 'Recycle'-logo, implemented
by Ian Green.

