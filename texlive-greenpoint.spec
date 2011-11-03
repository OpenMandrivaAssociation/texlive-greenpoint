# revision 15878
# category Package
# catalog-ctan /fonts/greenpoint
# catalog-date 2006-12-09 16:48:33 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-greenpoint
Version:	20061209
Release:	1
Summary:	The Green Point logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greenpoint
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A MetaFont-implementation of the logo commonly known as 'Der
Grune Punkt' ('The Green Point'). In Austria, it can be found
on nearly every bottle. It should not be confused with the
'Recycle'-logo, implemented by Ian Green.

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
%{_texmfdistdir}/fonts/source/public/greenpoint/greenpoint.mf
%{_texmfdistdir}/fonts/tfm/public/greenpoint/greenpoint.tfm
%doc %{_texmfdistdir}/doc/fonts/greenpoint/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/greenpoint/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
