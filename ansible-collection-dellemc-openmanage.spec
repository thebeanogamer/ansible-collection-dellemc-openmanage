%bcond tests %{undefined rhel}

Name:           ansible-collection-dellemc-openmanage
Version:        9.3.0
Release:        %autorelease
Summary:        Dell OpenManage collection for Ansible

License:        GPL-3.0-only
URL:            %{ansible_collection_url dellemc openmanage}
Source:         https://github.com/dell/dellemc-openmanage-ansible-modules/archive/v%{version}/dellemc-openmanage-%{version}.tar.gz
# build_ignore development files, tests, and docs
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(mock)
%endif

# From bindep.txt
Requires:       xorriso
Requires:       syslinux
Requires:       isomd5sum
Requires:       wget
Requires:       python3dist(omsdk)
Requires:       python3dist(netaddr)

%description
%{summary}.


%prep
%autosetup -p1 -n dellemc-openmanage-ansible-modules-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find . -type f -empty ! -name __init__.py -print -delete


%if %{with tests}
%generate_buildrequires
%pyproject_buildrequires -N requirements.txt
%endif


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%if %{with tests}
%ansible_test_unit
%endif


%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md CHANGELOG.rst* docs/*


%changelog
%autochangelog
