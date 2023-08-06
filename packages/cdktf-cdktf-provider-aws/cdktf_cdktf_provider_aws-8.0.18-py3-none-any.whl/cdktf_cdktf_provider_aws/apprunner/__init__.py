import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import cdktf
import constructs


class ApprunnerAutoScalingConfigurationVersion(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerAutoScalingConfigurationVersion",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version aws_apprunner_auto_scaling_configuration_version}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        auto_scaling_configuration_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version aws_apprunner_auto_scaling_configuration_version} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auto_scaling_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#auto_scaling_configuration_name ApprunnerAutoScalingConfigurationVersion#auto_scaling_configuration_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#id ApprunnerAutoScalingConfigurationVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#max_concurrency ApprunnerAutoScalingConfigurationVersion#max_concurrency}.
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#max_size ApprunnerAutoScalingConfigurationVersion#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#min_size ApprunnerAutoScalingConfigurationVersion#min_size}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#tags ApprunnerAutoScalingConfigurationVersion#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#tags_all ApprunnerAutoScalingConfigurationVersion#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ApprunnerAutoScalingConfigurationVersionConfig(
            auto_scaling_configuration_name=auto_scaling_configuration_name,
            id=id,
            max_concurrency=max_concurrency,
            max_size=max_size,
            min_size=min_size,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxConcurrency")
    def reset_max_concurrency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrency", []))

    @jsii.member(jsii_name="resetMaxSize")
    def reset_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSize", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationRevision")
    def auto_scaling_configuration_revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoScalingConfigurationRevision"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="latest")
    def latest(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "latest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationNameInput")
    def auto_scaling_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationName")
    def auto_scaling_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoScalingConfigurationName"))

    @auto_scaling_configuration_name.setter
    def auto_scaling_configuration_name(self, value: builtins.str) -> None:
        jsii.set(self, "autoScalingConfigurationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: jsii.Number) -> None:
        jsii.set(self, "maxConcurrency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        jsii.set(self, "maxSize", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        jsii.set(self, "minSize", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerAutoScalingConfigurationVersionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "auto_scaling_configuration_name": "autoScalingConfigurationName",
        "id": "id",
        "max_concurrency": "maxConcurrency",
        "max_size": "maxSize",
        "min_size": "minSize",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ApprunnerAutoScalingConfigurationVersionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        auto_scaling_configuration_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''App Runner.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param auto_scaling_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#auto_scaling_configuration_name ApprunnerAutoScalingConfigurationVersion#auto_scaling_configuration_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#id ApprunnerAutoScalingConfigurationVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#max_concurrency ApprunnerAutoScalingConfigurationVersion#max_concurrency}.
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#max_size ApprunnerAutoScalingConfigurationVersion#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#min_size ApprunnerAutoScalingConfigurationVersion#min_size}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#tags ApprunnerAutoScalingConfigurationVersion#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#tags_all ApprunnerAutoScalingConfigurationVersion#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "auto_scaling_configuration_name": auto_scaling_configuration_name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if id is not None:
            self._values["id"] = id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def auto_scaling_configuration_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#auto_scaling_configuration_name ApprunnerAutoScalingConfigurationVersion#auto_scaling_configuration_name}.'''
        result = self._values.get("auto_scaling_configuration_name")
        assert result is not None, "Required property 'auto_scaling_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#id ApprunnerAutoScalingConfigurationVersion#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#max_concurrency ApprunnerAutoScalingConfigurationVersion#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#max_size ApprunnerAutoScalingConfigurationVersion#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#min_size ApprunnerAutoScalingConfigurationVersion#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#tags ApprunnerAutoScalingConfigurationVersion#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_auto_scaling_configuration_version#tags_all ApprunnerAutoScalingConfigurationVersion#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerAutoScalingConfigurationVersionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection aws_apprunner_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        connection_name: builtins.str,
        provider_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection aws_apprunner_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#connection_name ApprunnerConnection#connection_name}.
        :param provider_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#provider_type ApprunnerConnection#provider_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#id ApprunnerConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#tags ApprunnerConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#tags_all ApprunnerConnection#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ApprunnerConnectionConfig(
            connection_name=connection_name,
            provider_type=provider_type,
            id=id,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerTypeInput")
    def provider_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        jsii.set(self, "connectionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerType")
    def provider_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerType"))

    @provider_type.setter
    def provider_type(self, value: builtins.str) -> None:
        jsii.set(self, "providerType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "connection_name": "connectionName",
        "provider_type": "providerType",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ApprunnerConnectionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        connection_name: builtins.str,
        provider_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''App Runner.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#connection_name ApprunnerConnection#connection_name}.
        :param provider_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#provider_type ApprunnerConnection#provider_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#id ApprunnerConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#tags ApprunnerConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#tags_all ApprunnerConnection#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "connection_name": connection_name,
            "provider_type": provider_type,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#connection_name ApprunnerConnection#connection_name}.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#provider_type ApprunnerConnection#provider_type}.'''
        result = self._values.get("provider_type")
        assert result is not None, "Required property 'provider_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#id ApprunnerConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#tags ApprunnerConnection#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_connection#tags_all ApprunnerConnection#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerCustomDomainAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerCustomDomainAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association aws_apprunner_custom_domain_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        service_arn: builtins.str,
        enable_www_subdomain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association aws_apprunner_custom_domain_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#domain_name ApprunnerCustomDomainAssociation#domain_name}.
        :param service_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#service_arn ApprunnerCustomDomainAssociation#service_arn}.
        :param enable_www_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#enable_www_subdomain ApprunnerCustomDomainAssociation#enable_www_subdomain}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#id ApprunnerCustomDomainAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ApprunnerCustomDomainAssociationConfig(
            domain_name=domain_name,
            service_arn=service_arn,
            enable_www_subdomain=enable_www_subdomain,
            id=id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEnableWwwSubdomain")
    def reset_enable_www_subdomain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableWwwSubdomain", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateValidationRecords")
    def certificate_validation_records(
        self,
    ) -> "ApprunnerCustomDomainAssociationCertificateValidationRecordsList":
        return typing.cast("ApprunnerCustomDomainAssociationCertificateValidationRecordsList", jsii.get(self, "certificateValidationRecords"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsTarget")
    def dns_target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsTarget"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableWwwSubdomainInput")
    def enable_www_subdomain_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableWwwSubdomainInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArnInput")
    def service_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableWwwSubdomain")
    def enable_www_subdomain(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableWwwSubdomain"))

    @enable_www_subdomain.setter
    def enable_www_subdomain(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "enableWwwSubdomain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceArn"))

    @service_arn.setter
    def service_arn(self, value: builtins.str) -> None:
        jsii.set(self, "serviceArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerCustomDomainAssociationCertificateValidationRecords",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApprunnerCustomDomainAssociationCertificateValidationRecords:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerCustomDomainAssociationCertificateValidationRecords(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerCustomDomainAssociationCertificateValidationRecordsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerCustomDomainAssociationCertificateValidationRecordsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApprunnerCustomDomainAssociationCertificateValidationRecordsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        return typing.cast("ApprunnerCustomDomainAssociationCertificateValidationRecordsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        jsii.set(self, "wrapsSet", value)


class ApprunnerCustomDomainAssociationCertificateValidationRecordsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerCustomDomainAssociationCertificateValidationRecordsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerCustomDomainAssociationCertificateValidationRecords]:
        return typing.cast(typing.Optional[ApprunnerCustomDomainAssociationCertificateValidationRecords], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerCustomDomainAssociationCertificateValidationRecords],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerCustomDomainAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "domain_name": "domainName",
        "service_arn": "serviceArn",
        "enable_www_subdomain": "enableWwwSubdomain",
        "id": "id",
    },
)
class ApprunnerCustomDomainAssociationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        domain_name: builtins.str,
        service_arn: builtins.str,
        enable_www_subdomain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''App Runner.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#domain_name ApprunnerCustomDomainAssociation#domain_name}.
        :param service_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#service_arn ApprunnerCustomDomainAssociation#service_arn}.
        :param enable_www_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#enable_www_subdomain ApprunnerCustomDomainAssociation#enable_www_subdomain}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#id ApprunnerCustomDomainAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "service_arn": service_arn,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if enable_www_subdomain is not None:
            self._values["enable_www_subdomain"] = enable_www_subdomain
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#domain_name ApprunnerCustomDomainAssociation#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#service_arn ApprunnerCustomDomainAssociation#service_arn}.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_www_subdomain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#enable_www_subdomain ApprunnerCustomDomainAssociation#enable_www_subdomain}.'''
        result = self._values.get("enable_www_subdomain")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_custom_domain_association#id ApprunnerCustomDomainAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerCustomDomainAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerObservabilityConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerObservabilityConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration aws_apprunner_observability_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        observability_configuration_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trace_configuration: typing.Optional["ApprunnerObservabilityConfigurationTraceConfiguration"] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration aws_apprunner_observability_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param observability_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#observability_configuration_name ApprunnerObservabilityConfiguration#observability_configuration_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#id ApprunnerObservabilityConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#tags ApprunnerObservabilityConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#tags_all ApprunnerObservabilityConfiguration#tags_all}.
        :param trace_configuration: trace_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#trace_configuration ApprunnerObservabilityConfiguration#trace_configuration}
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ApprunnerObservabilityConfigurationConfig(
            observability_configuration_name=observability_configuration_name,
            id=id,
            tags=tags,
            tags_all=tags_all,
            trace_configuration=trace_configuration,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTraceConfiguration")
    def put_trace_configuration(
        self,
        *,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param vendor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#vendor ApprunnerObservabilityConfiguration#vendor}.
        '''
        value = ApprunnerObservabilityConfigurationTraceConfiguration(vendor=vendor)

        return typing.cast(None, jsii.invoke(self, "putTraceConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTraceConfiguration")
    def reset_trace_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTraceConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="latest")
    def latest(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "latest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationRevision")
    def observability_configuration_revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "observabilityConfigurationRevision"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="traceConfiguration")
    def trace_configuration(
        self,
    ) -> "ApprunnerObservabilityConfigurationTraceConfigurationOutputReference":
        return typing.cast("ApprunnerObservabilityConfigurationTraceConfigurationOutputReference", jsii.get(self, "traceConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationNameInput")
    def observability_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "observabilityConfigurationNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="traceConfigurationInput")
    def trace_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerObservabilityConfigurationTraceConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerObservabilityConfigurationTraceConfiguration"], jsii.get(self, "traceConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationName")
    def observability_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "observabilityConfigurationName"))

    @observability_configuration_name.setter
    def observability_configuration_name(self, value: builtins.str) -> None:
        jsii.set(self, "observabilityConfigurationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerObservabilityConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "observability_configuration_name": "observabilityConfigurationName",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
        "trace_configuration": "traceConfiguration",
    },
)
class ApprunnerObservabilityConfigurationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        observability_configuration_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trace_configuration: typing.Optional["ApprunnerObservabilityConfigurationTraceConfiguration"] = None,
    ) -> None:
        '''App Runner.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param observability_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#observability_configuration_name ApprunnerObservabilityConfiguration#observability_configuration_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#id ApprunnerObservabilityConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#tags ApprunnerObservabilityConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#tags_all ApprunnerObservabilityConfiguration#tags_all}.
        :param trace_configuration: trace_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#trace_configuration ApprunnerObservabilityConfiguration#trace_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(trace_configuration, dict):
            trace_configuration = ApprunnerObservabilityConfigurationTraceConfiguration(**trace_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "observability_configuration_name": observability_configuration_name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if trace_configuration is not None:
            self._values["trace_configuration"] = trace_configuration

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def observability_configuration_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#observability_configuration_name ApprunnerObservabilityConfiguration#observability_configuration_name}.'''
        result = self._values.get("observability_configuration_name")
        assert result is not None, "Required property 'observability_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#id ApprunnerObservabilityConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#tags ApprunnerObservabilityConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#tags_all ApprunnerObservabilityConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def trace_configuration(
        self,
    ) -> typing.Optional["ApprunnerObservabilityConfigurationTraceConfiguration"]:
        '''trace_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#trace_configuration ApprunnerObservabilityConfiguration#trace_configuration}
        '''
        result = self._values.get("trace_configuration")
        return typing.cast(typing.Optional["ApprunnerObservabilityConfigurationTraceConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerObservabilityConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerObservabilityConfigurationTraceConfiguration",
    jsii_struct_bases=[],
    name_mapping={"vendor": "vendor"},
)
class ApprunnerObservabilityConfigurationTraceConfiguration:
    def __init__(self, *, vendor: typing.Optional[builtins.str] = None) -> None:
        '''
        :param vendor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#vendor ApprunnerObservabilityConfiguration#vendor}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_observability_configuration#vendor ApprunnerObservabilityConfiguration#vendor}.'''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerObservabilityConfigurationTraceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerObservabilityConfigurationTraceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerObservabilityConfigurationTraceConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetVendor")
    def reset_vendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendor", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vendorInput")
    def vendor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendorInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: builtins.str) -> None:
        jsii.set(self, "vendor", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerObservabilityConfigurationTraceConfiguration]:
        return typing.cast(typing.Optional[ApprunnerObservabilityConfigurationTraceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerObservabilityConfigurationTraceConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service aws_apprunner_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        service_name: builtins.str,
        source_configuration: "ApprunnerServiceSourceConfiguration",
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional["ApprunnerServiceEncryptionConfiguration"] = None,
        health_check_configuration: typing.Optional["ApprunnerServiceHealthCheckConfiguration"] = None,
        id: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional["ApprunnerServiceInstanceConfiguration"] = None,
        network_configuration: typing.Optional["ApprunnerServiceNetworkConfiguration"] = None,
        observability_configuration: typing.Optional["ApprunnerServiceObservabilityConfiguration"] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service aws_apprunner_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#service_name ApprunnerService#service_name}.
        :param source_configuration: source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#source_configuration ApprunnerService#source_configuration}
        :param auto_scaling_configuration_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#auto_scaling_configuration_arn ApprunnerService#auto_scaling_configuration_arn}.
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#encryption_configuration ApprunnerService#encryption_configuration}
        :param health_check_configuration: health_check_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#health_check_configuration ApprunnerService#health_check_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#id ApprunnerService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_configuration: instance_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#instance_configuration ApprunnerService#instance_configuration}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#network_configuration ApprunnerService#network_configuration}
        :param observability_configuration: observability_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_configuration ApprunnerService#observability_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#tags ApprunnerService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#tags_all ApprunnerService#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ApprunnerServiceConfig(
            service_name=service_name,
            source_configuration=source_configuration,
            auto_scaling_configuration_arn=auto_scaling_configuration_arn,
            encryption_configuration=encryption_configuration,
            health_check_configuration=health_check_configuration,
            id=id,
            instance_configuration=instance_configuration,
            network_configuration=network_configuration,
            observability_configuration=observability_configuration,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEncryptionConfiguration")
    def put_encryption_configuration(self, *, kms_key: builtins.str) -> None:
        '''
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#kms_key ApprunnerService#kms_key}.
        '''
        value = ApprunnerServiceEncryptionConfiguration(kms_key=kms_key)

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putHealthCheckConfiguration")
    def put_health_check_configuration(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#healthy_threshold ApprunnerService#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#interval ApprunnerService#interval}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#path ApprunnerService#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#protocol ApprunnerService#protocol}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#timeout ApprunnerService#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#unhealthy_threshold ApprunnerService#unhealthy_threshold}.
        '''
        value = ApprunnerServiceHealthCheckConfiguration(
            healthy_threshold=healthy_threshold,
            interval=interval,
            path=path,
            protocol=protocol,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheckConfiguration", [value]))

    @jsii.member(jsii_name="putInstanceConfiguration")
    def put_instance_configuration(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#cpu ApprunnerService#cpu}.
        :param instance_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#instance_role_arn ApprunnerService#instance_role_arn}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#memory ApprunnerService#memory}.
        '''
        value = ApprunnerServiceInstanceConfiguration(
            cpu=cpu, instance_role_arn=instance_role_arn, memory=memory
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceConfiguration", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        egress_configuration: typing.Optional["ApprunnerServiceNetworkConfigurationEgressConfiguration"] = None,
    ) -> None:
        '''
        :param egress_configuration: egress_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#egress_configuration ApprunnerService#egress_configuration}
        '''
        value = ApprunnerServiceNetworkConfiguration(
            egress_configuration=egress_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putObservabilityConfiguration")
    def put_observability_configuration(
        self,
        *,
        observability_configuration_arn: builtins.str,
        observability_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param observability_configuration_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_configuration_arn ApprunnerService#observability_configuration_arn}.
        :param observability_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_enabled ApprunnerService#observability_enabled}.
        '''
        value = ApprunnerServiceObservabilityConfiguration(
            observability_configuration_arn=observability_configuration_arn,
            observability_enabled=observability_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putObservabilityConfiguration", [value]))

    @jsii.member(jsii_name="putSourceConfiguration")
    def put_source_configuration(
        self,
        *,
        authentication_configuration: typing.Optional["ApprunnerServiceSourceConfigurationAuthenticationConfiguration"] = None,
        auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        code_repository: typing.Optional["ApprunnerServiceSourceConfigurationCodeRepository"] = None,
        image_repository: typing.Optional["ApprunnerServiceSourceConfigurationImageRepository"] = None,
    ) -> None:
        '''
        :param authentication_configuration: authentication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#authentication_configuration ApprunnerService#authentication_configuration}
        :param auto_deployments_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#auto_deployments_enabled ApprunnerService#auto_deployments_enabled}.
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_repository ApprunnerService#code_repository}
        :param image_repository: image_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_repository ApprunnerService#image_repository}
        '''
        value = ApprunnerServiceSourceConfiguration(
            authentication_configuration=authentication_configuration,
            auto_deployments_enabled=auto_deployments_enabled,
            code_repository=code_repository,
            image_repository=image_repository,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceConfiguration", [value]))

    @jsii.member(jsii_name="resetAutoScalingConfigurationArn")
    def reset_auto_scaling_configuration_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScalingConfigurationArn", []))

    @jsii.member(jsii_name="resetEncryptionConfiguration")
    def reset_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetHealthCheckConfiguration")
    def reset_health_check_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceConfiguration")
    def reset_instance_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceConfiguration", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetObservabilityConfiguration")
    def reset_observability_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObservabilityConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> "ApprunnerServiceEncryptionConfigurationOutputReference":
        return typing.cast("ApprunnerServiceEncryptionConfigurationOutputReference", jsii.get(self, "encryptionConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> "ApprunnerServiceHealthCheckConfigurationOutputReference":
        return typing.cast("ApprunnerServiceHealthCheckConfigurationOutputReference", jsii.get(self, "healthCheckConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> "ApprunnerServiceInstanceConfigurationOutputReference":
        return typing.cast("ApprunnerServiceInstanceConfigurationOutputReference", jsii.get(self, "instanceConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> "ApprunnerServiceNetworkConfigurationOutputReference":
        return typing.cast("ApprunnerServiceNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfiguration")
    def observability_configuration(
        self,
    ) -> "ApprunnerServiceObservabilityConfigurationOutputReference":
        return typing.cast("ApprunnerServiceObservabilityConfigurationOutputReference", jsii.get(self, "observabilityConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceUrl")
    def service_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> "ApprunnerServiceSourceConfigurationOutputReference":
        return typing.cast("ApprunnerServiceSourceConfigurationOutputReference", jsii.get(self, "sourceConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationArnInput")
    def auto_scaling_configuration_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfigurationInput")
    def encryption_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerServiceEncryptionConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerServiceEncryptionConfiguration"], jsii.get(self, "encryptionConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckConfigurationInput")
    def health_check_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerServiceHealthCheckConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerServiceHealthCheckConfiguration"], jsii.get(self, "healthCheckConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceConfigurationInput")
    def instance_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerServiceInstanceConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerServiceInstanceConfiguration"], jsii.get(self, "instanceConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerServiceNetworkConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerServiceNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationInput")
    def observability_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerServiceObservabilityConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerServiceObservabilityConfiguration"], jsii.get(self, "observabilityConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceConfigurationInput")
    def source_configuration_input(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfiguration"]:
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfiguration"], jsii.get(self, "sourceConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoScalingConfigurationArn"))

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(self, value: builtins.str) -> None:
        jsii.set(self, "autoScalingConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        jsii.set(self, "serviceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "service_name": "serviceName",
        "source_configuration": "sourceConfiguration",
        "auto_scaling_configuration_arn": "autoScalingConfigurationArn",
        "encryption_configuration": "encryptionConfiguration",
        "health_check_configuration": "healthCheckConfiguration",
        "id": "id",
        "instance_configuration": "instanceConfiguration",
        "network_configuration": "networkConfiguration",
        "observability_configuration": "observabilityConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ApprunnerServiceConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        service_name: builtins.str,
        source_configuration: "ApprunnerServiceSourceConfiguration",
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional["ApprunnerServiceEncryptionConfiguration"] = None,
        health_check_configuration: typing.Optional["ApprunnerServiceHealthCheckConfiguration"] = None,
        id: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional["ApprunnerServiceInstanceConfiguration"] = None,
        network_configuration: typing.Optional["ApprunnerServiceNetworkConfiguration"] = None,
        observability_configuration: typing.Optional["ApprunnerServiceObservabilityConfiguration"] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''App Runner.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#service_name ApprunnerService#service_name}.
        :param source_configuration: source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#source_configuration ApprunnerService#source_configuration}
        :param auto_scaling_configuration_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#auto_scaling_configuration_arn ApprunnerService#auto_scaling_configuration_arn}.
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#encryption_configuration ApprunnerService#encryption_configuration}
        :param health_check_configuration: health_check_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#health_check_configuration ApprunnerService#health_check_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#id ApprunnerService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_configuration: instance_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#instance_configuration ApprunnerService#instance_configuration}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#network_configuration ApprunnerService#network_configuration}
        :param observability_configuration: observability_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_configuration ApprunnerService#observability_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#tags ApprunnerService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#tags_all ApprunnerService#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(source_configuration, dict):
            source_configuration = ApprunnerServiceSourceConfiguration(**source_configuration)
        if isinstance(encryption_configuration, dict):
            encryption_configuration = ApprunnerServiceEncryptionConfiguration(**encryption_configuration)
        if isinstance(health_check_configuration, dict):
            health_check_configuration = ApprunnerServiceHealthCheckConfiguration(**health_check_configuration)
        if isinstance(instance_configuration, dict):
            instance_configuration = ApprunnerServiceInstanceConfiguration(**instance_configuration)
        if isinstance(network_configuration, dict):
            network_configuration = ApprunnerServiceNetworkConfiguration(**network_configuration)
        if isinstance(observability_configuration, dict):
            observability_configuration = ApprunnerServiceObservabilityConfiguration(**observability_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "service_name": service_name,
            "source_configuration": source_configuration,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if auto_scaling_configuration_arn is not None:
            self._values["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if health_check_configuration is not None:
            self._values["health_check_configuration"] = health_check_configuration
        if id is not None:
            self._values["id"] = id
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if observability_configuration is not None:
            self._values["observability_configuration"] = observability_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#service_name ApprunnerService#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_configuration(self) -> "ApprunnerServiceSourceConfiguration":
        '''source_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#source_configuration ApprunnerService#source_configuration}
        '''
        result = self._values.get("source_configuration")
        assert result is not None, "Required property 'source_configuration' is missing"
        return typing.cast("ApprunnerServiceSourceConfiguration", result)

    @builtins.property
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#auto_scaling_configuration_arn ApprunnerService#auto_scaling_configuration_arn}.'''
        result = self._values.get("auto_scaling_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceEncryptionConfiguration"]:
        '''encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#encryption_configuration ApprunnerService#encryption_configuration}
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceEncryptionConfiguration"], result)

    @builtins.property
    def health_check_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceHealthCheckConfiguration"]:
        '''health_check_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#health_check_configuration ApprunnerService#health_check_configuration}
        '''
        result = self._values.get("health_check_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceHealthCheckConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#id ApprunnerService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceInstanceConfiguration"]:
        '''instance_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#instance_configuration ApprunnerService#instance_configuration}
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceInstanceConfiguration"], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#network_configuration ApprunnerService#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceNetworkConfiguration"], result)

    @builtins.property
    def observability_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceObservabilityConfiguration"]:
        '''observability_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_configuration ApprunnerService#observability_configuration}
        '''
        result = self._values.get("observability_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceObservabilityConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#tags ApprunnerService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#tags_all ApprunnerService#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key": "kmsKey"},
)
class ApprunnerServiceEncryptionConfiguration:
    def __init__(self, *, kms_key: builtins.str) -> None:
        '''
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#kms_key ApprunnerService#kms_key}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key": kms_key,
        }

    @builtins.property
    def kms_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#kms_key ApprunnerService#kms_key}.'''
        result = self._values.get("kms_key")
        assert result is not None, "Required property 'kms_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceEncryptionConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        jsii.set(self, "kmsKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceEncryptionConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceEncryptionConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceHealthCheckConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "path": "path",
        "protocol": "protocol",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class ApprunnerServiceHealthCheckConfiguration:
    def __init__(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#healthy_threshold ApprunnerService#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#interval ApprunnerService#interval}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#path ApprunnerService#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#protocol ApprunnerService#protocol}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#timeout ApprunnerService#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#unhealthy_threshold ApprunnerService#unhealthy_threshold}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval is not None:
            self._values["interval"] = interval
        if path is not None:
            self._values["path"] = path
        if protocol is not None:
            self._values["protocol"] = protocol
        if timeout is not None:
            self._values["timeout"] = timeout
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#healthy_threshold ApprunnerService#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#interval ApprunnerService#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#path ApprunnerService#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#protocol ApprunnerService#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#timeout ApprunnerService#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#unhealthy_threshold ApprunnerService#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceHealthCheckConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceHealthCheckConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceHealthCheckConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        jsii.set(self, "healthyThreshold", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        jsii.set(self, "interval", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        jsii.set(self, "path", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        jsii.set(self, "protocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        jsii.set(self, "timeout", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceHealthCheckConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceHealthCheckConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceHealthCheckConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceInstanceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cpu": "cpu",
        "instance_role_arn": "instanceRoleArn",
        "memory": "memory",
    },
)
class ApprunnerServiceInstanceConfiguration:
    def __init__(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#cpu ApprunnerService#cpu}.
        :param instance_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#instance_role_arn ApprunnerService#instance_role_arn}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#memory ApprunnerService#memory}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if instance_role_arn is not None:
            self._values["instance_role_arn"] = instance_role_arn
        if memory is not None:
            self._values["memory"] = memory

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#cpu ApprunnerService#cpu}.'''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#instance_role_arn ApprunnerService#instance_role_arn}.'''
        result = self._values.get("instance_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#memory ApprunnerService#memory}.'''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceInstanceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceInstanceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceInstanceConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetInstanceRoleArn")
    def reset_instance_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRoleArn", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceRoleArnInput")
    def instance_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        jsii.set(self, "cpu", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceRoleArn")
    def instance_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceRoleArn"))

    @instance_role_arn.setter
    def instance_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        jsii.set(self, "memory", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApprunnerServiceInstanceConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceInstanceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceInstanceConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={"egress_configuration": "egressConfiguration"},
)
class ApprunnerServiceNetworkConfiguration:
    def __init__(
        self,
        *,
        egress_configuration: typing.Optional["ApprunnerServiceNetworkConfigurationEgressConfiguration"] = None,
    ) -> None:
        '''
        :param egress_configuration: egress_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#egress_configuration ApprunnerService#egress_configuration}
        '''
        if isinstance(egress_configuration, dict):
            egress_configuration = ApprunnerServiceNetworkConfigurationEgressConfiguration(**egress_configuration)
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_configuration is not None:
            self._values["egress_configuration"] = egress_configuration

    @builtins.property
    def egress_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceNetworkConfigurationEgressConfiguration"]:
        '''egress_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#egress_configuration ApprunnerService#egress_configuration}
        '''
        result = self._values.get("egress_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceNetworkConfigurationEgressConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceNetworkConfigurationEgressConfiguration",
    jsii_struct_bases=[],
    name_mapping={"egress_type": "egressType", "vpc_connector_arn": "vpcConnectorArn"},
)
class ApprunnerServiceNetworkConfigurationEgressConfiguration:
    def __init__(
        self,
        *,
        egress_type: typing.Optional[builtins.str] = None,
        vpc_connector_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param egress_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#egress_type ApprunnerService#egress_type}.
        :param vpc_connector_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#vpc_connector_arn ApprunnerService#vpc_connector_arn}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_type is not None:
            self._values["egress_type"] = egress_type
        if vpc_connector_arn is not None:
            self._values["vpc_connector_arn"] = vpc_connector_arn

    @builtins.property
    def egress_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#egress_type ApprunnerService#egress_type}.'''
        result = self._values.get("egress_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_connector_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#vpc_connector_arn ApprunnerService#vpc_connector_arn}.'''
        result = self._values.get("vpc_connector_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceNetworkConfigurationEgressConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceNetworkConfigurationEgressConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceNetworkConfigurationEgressConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEgressType")
    def reset_egress_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressType", []))

    @jsii.member(jsii_name="resetVpcConnectorArn")
    def reset_vpc_connector_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConnectorArn", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="egressTypeInput")
    def egress_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "egressTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectorArnInput")
    def vpc_connector_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcConnectorArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="egressType")
    def egress_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egressType"))

    @egress_type.setter
    def egress_type(self, value: builtins.str) -> None:
        jsii.set(self, "egressType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectorArn")
    def vpc_connector_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcConnectorArn"))

    @vpc_connector_arn.setter
    def vpc_connector_arn(self, value: builtins.str) -> None:
        jsii.set(self, "vpcConnectorArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceNetworkConfigurationEgressConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceNetworkConfigurationEgressConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceNetworkConfigurationEgressConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerServiceNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceNetworkConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEgressConfiguration")
    def put_egress_configuration(
        self,
        *,
        egress_type: typing.Optional[builtins.str] = None,
        vpc_connector_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param egress_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#egress_type ApprunnerService#egress_type}.
        :param vpc_connector_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#vpc_connector_arn ApprunnerService#vpc_connector_arn}.
        '''
        value = ApprunnerServiceNetworkConfigurationEgressConfiguration(
            egress_type=egress_type, vpc_connector_arn=vpc_connector_arn
        )

        return typing.cast(None, jsii.invoke(self, "putEgressConfiguration", [value]))

    @jsii.member(jsii_name="resetEgressConfiguration")
    def reset_egress_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressConfiguration", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="egressConfiguration")
    def egress_configuration(
        self,
    ) -> ApprunnerServiceNetworkConfigurationEgressConfigurationOutputReference:
        return typing.cast(ApprunnerServiceNetworkConfigurationEgressConfigurationOutputReference, jsii.get(self, "egressConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="egressConfigurationInput")
    def egress_configuration_input(
        self,
    ) -> typing.Optional[ApprunnerServiceNetworkConfigurationEgressConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceNetworkConfigurationEgressConfiguration], jsii.get(self, "egressConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApprunnerServiceNetworkConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceNetworkConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceObservabilityConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "observability_configuration_arn": "observabilityConfigurationArn",
        "observability_enabled": "observabilityEnabled",
    },
)
class ApprunnerServiceObservabilityConfiguration:
    def __init__(
        self,
        *,
        observability_configuration_arn: builtins.str,
        observability_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param observability_configuration_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_configuration_arn ApprunnerService#observability_configuration_arn}.
        :param observability_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_enabled ApprunnerService#observability_enabled}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "observability_configuration_arn": observability_configuration_arn,
            "observability_enabled": observability_enabled,
        }

    @builtins.property
    def observability_configuration_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_configuration_arn ApprunnerService#observability_configuration_arn}.'''
        result = self._values.get("observability_configuration_arn")
        assert result is not None, "Required property 'observability_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def observability_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#observability_enabled ApprunnerService#observability_enabled}.'''
        result = self._values.get("observability_enabled")
        assert result is not None, "Required property 'observability_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceObservabilityConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceObservabilityConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceObservabilityConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationArnInput")
    def observability_configuration_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "observabilityConfigurationArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityEnabledInput")
    def observability_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "observabilityEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationArn")
    def observability_configuration_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "observabilityConfigurationArn"))

    @observability_configuration_arn.setter
    def observability_configuration_arn(self, value: builtins.str) -> None:
        jsii.set(self, "observabilityConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityEnabled")
    def observability_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "observabilityEnabled"))

    @observability_enabled.setter
    def observability_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "observabilityEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceObservabilityConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceObservabilityConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceObservabilityConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_configuration": "authenticationConfiguration",
        "auto_deployments_enabled": "autoDeploymentsEnabled",
        "code_repository": "codeRepository",
        "image_repository": "imageRepository",
    },
)
class ApprunnerServiceSourceConfiguration:
    def __init__(
        self,
        *,
        authentication_configuration: typing.Optional["ApprunnerServiceSourceConfigurationAuthenticationConfiguration"] = None,
        auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        code_repository: typing.Optional["ApprunnerServiceSourceConfigurationCodeRepository"] = None,
        image_repository: typing.Optional["ApprunnerServiceSourceConfigurationImageRepository"] = None,
    ) -> None:
        '''
        :param authentication_configuration: authentication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#authentication_configuration ApprunnerService#authentication_configuration}
        :param auto_deployments_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#auto_deployments_enabled ApprunnerService#auto_deployments_enabled}.
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_repository ApprunnerService#code_repository}
        :param image_repository: image_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_repository ApprunnerService#image_repository}
        '''
        if isinstance(authentication_configuration, dict):
            authentication_configuration = ApprunnerServiceSourceConfigurationAuthenticationConfiguration(**authentication_configuration)
        if isinstance(code_repository, dict):
            code_repository = ApprunnerServiceSourceConfigurationCodeRepository(**code_repository)
        if isinstance(image_repository, dict):
            image_repository = ApprunnerServiceSourceConfigurationImageRepository(**image_repository)
        self._values: typing.Dict[str, typing.Any] = {}
        if authentication_configuration is not None:
            self._values["authentication_configuration"] = authentication_configuration
        if auto_deployments_enabled is not None:
            self._values["auto_deployments_enabled"] = auto_deployments_enabled
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if image_repository is not None:
            self._values["image_repository"] = image_repository

    @builtins.property
    def authentication_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationAuthenticationConfiguration"]:
        '''authentication_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#authentication_configuration ApprunnerService#authentication_configuration}
        '''
        result = self._values.get("authentication_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationAuthenticationConfiguration"], result)

    @builtins.property
    def auto_deployments_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#auto_deployments_enabled ApprunnerService#auto_deployments_enabled}.'''
        result = self._values.get("auto_deployments_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def code_repository(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationCodeRepository"]:
        '''code_repository block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_repository ApprunnerService#code_repository}
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationCodeRepository"], result)

    @builtins.property
    def image_repository(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationImageRepository"]:
        '''image_repository block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_repository ApprunnerService#image_repository}
        '''
        result = self._values.get("image_repository")
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationImageRepository"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationAuthenticationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "access_role_arn": "accessRoleArn",
        "connection_arn": "connectionArn",
    },
)
class ApprunnerServiceSourceConfigurationAuthenticationConfiguration:
    def __init__(
        self,
        *,
        access_role_arn: typing.Optional[builtins.str] = None,
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#access_role_arn ApprunnerService#access_role_arn}.
        :param connection_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#connection_arn ApprunnerService#connection_arn}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if access_role_arn is not None:
            self._values["access_role_arn"] = access_role_arn
        if connection_arn is not None:
            self._values["connection_arn"] = connection_arn

    @builtins.property
    def access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#access_role_arn ApprunnerService#access_role_arn}.'''
        result = self._values.get("access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#connection_arn ApprunnerService#connection_arn}.'''
        result = self._values.get("connection_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationAuthenticationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceSourceConfigurationAuthenticationConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationAuthenticationConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessRoleArn")
    def reset_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessRoleArn", []))

    @jsii.member(jsii_name="resetConnectionArn")
    def reset_connection_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionArn", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessRoleArnInput")
    def access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessRoleArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionArnInput")
    def connection_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessRoleArn")
    def access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessRoleArn"))

    @access_role_arn.setter
    def access_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "accessRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: builtins.str) -> None:
        jsii.set(self, "connectionArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationAuthenticationConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationAuthenticationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationAuthenticationConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepository",
    jsii_struct_bases=[],
    name_mapping={
        "repository_url": "repositoryUrl",
        "source_code_version": "sourceCodeVersion",
        "code_configuration": "codeConfiguration",
    },
)
class ApprunnerServiceSourceConfigurationCodeRepository:
    def __init__(
        self,
        *,
        repository_url: builtins.str,
        source_code_version: "ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion",
        code_configuration: typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration"] = None,
    ) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#repository_url ApprunnerService#repository_url}.
        :param source_code_version: source_code_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#source_code_version ApprunnerService#source_code_version}
        :param code_configuration: code_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_configuration ApprunnerService#code_configuration}
        '''
        if isinstance(source_code_version, dict):
            source_code_version = ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion(**source_code_version)
        if isinstance(code_configuration, dict):
            code_configuration = ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration(**code_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "repository_url": repository_url,
            "source_code_version": source_code_version,
        }
        if code_configuration is not None:
            self._values["code_configuration"] = code_configuration

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#repository_url ApprunnerService#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_code_version(
        self,
    ) -> "ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion":
        '''source_code_version block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#source_code_version ApprunnerService#source_code_version}
        '''
        result = self._values.get("source_code_version")
        assert result is not None, "Required property 'source_code_version' is missing"
        return typing.cast("ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion", result)

    @builtins.property
    def code_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration"]:
        '''code_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_configuration ApprunnerService#code_configuration}
        '''
        result = self._values.get("code_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationCodeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_source": "configurationSource",
        "code_configuration_values": "codeConfigurationValues",
    },
)
class ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration:
    def __init__(
        self,
        *,
        configuration_source: builtins.str,
        code_configuration_values: typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues"] = None,
    ) -> None:
        '''
        :param configuration_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#configuration_source ApprunnerService#configuration_source}.
        :param code_configuration_values: code_configuration_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_configuration_values ApprunnerService#code_configuration_values}
        '''
        if isinstance(code_configuration_values, dict):
            code_configuration_values = ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues(**code_configuration_values)
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_source": configuration_source,
        }
        if code_configuration_values is not None:
            self._values["code_configuration_values"] = code_configuration_values

    @builtins.property
    def configuration_source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#configuration_source ApprunnerService#configuration_source}.'''
        result = self._values.get("configuration_source")
        assert result is not None, "Required property 'configuration_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_configuration_values(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues"]:
        '''code_configuration_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_configuration_values ApprunnerService#code_configuration_values}
        '''
        result = self._values.get("code_configuration_values")
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues",
    jsii_struct_bases=[],
    name_mapping={
        "runtime": "runtime",
        "build_command": "buildCommand",
        "port": "port",
        "runtime_environment_variables": "runtimeEnvironmentVariables",
        "start_command": "startCommand",
    },
)
class ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues:
    def __init__(
        self,
        *,
        runtime: builtins.str,
        build_command: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        runtime_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        start_command: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime ApprunnerService#runtime}.
        :param build_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#build_command ApprunnerService#build_command}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#port ApprunnerService#port}.
        :param runtime_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime_environment_variables ApprunnerService#runtime_environment_variables}.
        :param start_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#start_command ApprunnerService#start_command}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "runtime": runtime,
        }
        if build_command is not None:
            self._values["build_command"] = build_command
        if port is not None:
            self._values["port"] = port
        if runtime_environment_variables is not None:
            self._values["runtime_environment_variables"] = runtime_environment_variables
        if start_command is not None:
            self._values["start_command"] = start_command

    @builtins.property
    def runtime(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime ApprunnerService#runtime}.'''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#build_command ApprunnerService#build_command}.'''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#port ApprunnerService#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime_environment_variables ApprunnerService#runtime_environment_variables}.'''
        result = self._values.get("runtime_environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def start_command(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#start_command ApprunnerService#start_command}.'''
        result = self._values.get("start_command")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetRuntimeEnvironmentVariables")
    def reset_runtime_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeEnvironmentVariables", []))

    @jsii.member(jsii_name="resetStartCommand")
    def reset_start_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartCommand", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runtimeEnvironmentVariablesInput")
    def runtime_environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "runtimeEnvironmentVariablesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startCommandInput")
    def start_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startCommandInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        jsii.set(self, "buildCommand", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        jsii.set(self, "port", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        jsii.set(self, "runtime", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runtimeEnvironmentVariables")
    def runtime_environment_variables(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "runtimeEnvironmentVariables"))

    @runtime_environment_variables.setter
    def runtime_environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        jsii.set(self, "runtimeEnvironmentVariables", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startCommand")
    def start_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startCommand"))

    @start_command.setter
    def start_command(self, value: builtins.str) -> None:
        jsii.set(self, "startCommand", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeConfigurationValues")
    def put_code_configuration_values(
        self,
        *,
        runtime: builtins.str,
        build_command: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        runtime_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        start_command: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime ApprunnerService#runtime}.
        :param build_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#build_command ApprunnerService#build_command}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#port ApprunnerService#port}.
        :param runtime_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime_environment_variables ApprunnerService#runtime_environment_variables}.
        :param start_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#start_command ApprunnerService#start_command}.
        '''
        value = ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues(
            runtime=runtime,
            build_command=build_command,
            port=port,
            runtime_environment_variables=runtime_environment_variables,
            start_command=start_command,
        )

        return typing.cast(None, jsii.invoke(self, "putCodeConfigurationValues", [value]))

    @jsii.member(jsii_name="resetCodeConfigurationValues")
    def reset_code_configuration_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeConfigurationValues", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeConfigurationValues")
    def code_configuration_values(
        self,
    ) -> ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesOutputReference:
        return typing.cast(ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesOutputReference, jsii.get(self, "codeConfigurationValues"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeConfigurationValuesInput")
    def code_configuration_values_input(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues], jsii.get(self, "codeConfigurationValuesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSourceInput")
    def configuration_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationSourceInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSource")
    def configuration_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationSource"))

    @configuration_source.setter
    def configuration_source(self, value: builtins.str) -> None:
        jsii.set(self, "configurationSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerServiceSourceConfigurationCodeRepositoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeConfiguration")
    def put_code_configuration(
        self,
        *,
        configuration_source: builtins.str,
        code_configuration_values: typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues] = None,
    ) -> None:
        '''
        :param configuration_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#configuration_source ApprunnerService#configuration_source}.
        :param code_configuration_values: code_configuration_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_configuration_values ApprunnerService#code_configuration_values}
        '''
        value = ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration(
            configuration_source=configuration_source,
            code_configuration_values=code_configuration_values,
        )

        return typing.cast(None, jsii.invoke(self, "putCodeConfiguration", [value]))

    @jsii.member(jsii_name="putSourceCodeVersion")
    def put_source_code_version(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#type ApprunnerService#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#value ApprunnerService#value}.
        '''
        value_ = ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion(
            type=type, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putSourceCodeVersion", [value_]))

    @jsii.member(jsii_name="resetCodeConfiguration")
    def reset_code_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeConfiguration", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeConfiguration")
    def code_configuration(
        self,
    ) -> ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationOutputReference:
        return typing.cast(ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationOutputReference, jsii.get(self, "codeConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceCodeVersion")
    def source_code_version(
        self,
    ) -> "ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersionOutputReference":
        return typing.cast("ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersionOutputReference", jsii.get(self, "sourceCodeVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeConfigurationInput")
    def code_configuration_input(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration], jsii.get(self, "codeConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceCodeVersionInput")
    def source_code_version_input(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion"]:
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion"], jsii.get(self, "sourceCodeVersionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        jsii.set(self, "repositoryUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepository]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepository], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationCodeRepository],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion:
    def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#type ApprunnerService#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#value ApprunnerService#value}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#type ApprunnerService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#value ApprunnerService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        jsii.set(self, "value", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationImageRepository",
    jsii_struct_bases=[],
    name_mapping={
        "image_identifier": "imageIdentifier",
        "image_repository_type": "imageRepositoryType",
        "image_configuration": "imageConfiguration",
    },
)
class ApprunnerServiceSourceConfigurationImageRepository:
    def __init__(
        self,
        *,
        image_identifier: builtins.str,
        image_repository_type: builtins.str,
        image_configuration: typing.Optional["ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration"] = None,
    ) -> None:
        '''
        :param image_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_identifier ApprunnerService#image_identifier}.
        :param image_repository_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_repository_type ApprunnerService#image_repository_type}.
        :param image_configuration: image_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_configuration ApprunnerService#image_configuration}
        '''
        if isinstance(image_configuration, dict):
            image_configuration = ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration(**image_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "image_identifier": image_identifier,
            "image_repository_type": image_repository_type,
        }
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration

    @builtins.property
    def image_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_identifier ApprunnerService#image_identifier}.'''
        result = self._values.get("image_identifier")
        assert result is not None, "Required property 'image_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_repository_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_repository_type ApprunnerService#image_repository_type}.'''
        result = self._values.get("image_repository_type")
        assert result is not None, "Required property 'image_repository_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_configuration(
        self,
    ) -> typing.Optional["ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration"]:
        '''image_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_configuration ApprunnerService#image_configuration}
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional["ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationImageRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "runtime_environment_variables": "runtimeEnvironmentVariables",
        "start_command": "startCommand",
    },
)
class ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration:
    def __init__(
        self,
        *,
        port: typing.Optional[builtins.str] = None,
        runtime_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        start_command: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#port ApprunnerService#port}.
        :param runtime_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime_environment_variables ApprunnerService#runtime_environment_variables}.
        :param start_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#start_command ApprunnerService#start_command}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if runtime_environment_variables is not None:
            self._values["runtime_environment_variables"] = runtime_environment_variables
        if start_command is not None:
            self._values["start_command"] = start_command

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#port ApprunnerService#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime_environment_variables ApprunnerService#runtime_environment_variables}.'''
        result = self._values.get("runtime_environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def start_command(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#start_command ApprunnerService#start_command}.'''
        result = self._values.get("start_command")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprunnerServiceSourceConfigurationImageRepositoryImageConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationImageRepositoryImageConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetRuntimeEnvironmentVariables")
    def reset_runtime_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeEnvironmentVariables", []))

    @jsii.member(jsii_name="resetStartCommand")
    def reset_start_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartCommand", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runtimeEnvironmentVariablesInput")
    def runtime_environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "runtimeEnvironmentVariablesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startCommandInput")
    def start_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startCommandInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        jsii.set(self, "port", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runtimeEnvironmentVariables")
    def runtime_environment_variables(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "runtimeEnvironmentVariables"))

    @runtime_environment_variables.setter
    def runtime_environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        jsii.set(self, "runtimeEnvironmentVariables", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startCommand")
    def start_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startCommand"))

    @start_command.setter
    def start_command(self, value: builtins.str) -> None:
        jsii.set(self, "startCommand", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerServiceSourceConfigurationImageRepositoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationImageRepositoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putImageConfiguration")
    def put_image_configuration(
        self,
        *,
        port: typing.Optional[builtins.str] = None,
        runtime_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        start_command: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#port ApprunnerService#port}.
        :param runtime_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#runtime_environment_variables ApprunnerService#runtime_environment_variables}.
        :param start_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#start_command ApprunnerService#start_command}.
        '''
        value = ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration(
            port=port,
            runtime_environment_variables=runtime_environment_variables,
            start_command=start_command,
        )

        return typing.cast(None, jsii.invoke(self, "putImageConfiguration", [value]))

    @jsii.member(jsii_name="resetImageConfiguration")
    def reset_image_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageConfiguration", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageConfiguration")
    def image_configuration(
        self,
    ) -> ApprunnerServiceSourceConfigurationImageRepositoryImageConfigurationOutputReference:
        return typing.cast(ApprunnerServiceSourceConfigurationImageRepositoryImageConfigurationOutputReference, jsii.get(self, "imageConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageConfigurationInput")
    def image_configuration_input(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration], jsii.get(self, "imageConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageIdentifierInput")
    def image_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageIdentifierInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRepositoryTypeInput")
    def image_repository_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRepositoryTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageIdentifier")
    def image_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageIdentifier"))

    @image_identifier.setter
    def image_identifier(self, value: builtins.str) -> None:
        jsii.set(self, "imageIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRepositoryType")
    def image_repository_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageRepositoryType"))

    @image_repository_type.setter
    def image_repository_type(self, value: builtins.str) -> None:
        jsii.set(self, "imageRepositoryType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationImageRepository]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationImageRepository], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfigurationImageRepository],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerServiceSourceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerServiceSourceConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthenticationConfiguration")
    def put_authentication_configuration(
        self,
        *,
        access_role_arn: typing.Optional[builtins.str] = None,
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#access_role_arn ApprunnerService#access_role_arn}.
        :param connection_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#connection_arn ApprunnerService#connection_arn}.
        '''
        value = ApprunnerServiceSourceConfigurationAuthenticationConfiguration(
            access_role_arn=access_role_arn, connection_arn=connection_arn
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticationConfiguration", [value]))

    @jsii.member(jsii_name="putCodeRepository")
    def put_code_repository(
        self,
        *,
        repository_url: builtins.str,
        source_code_version: ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion,
        code_configuration: typing.Optional[ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration] = None,
    ) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#repository_url ApprunnerService#repository_url}.
        :param source_code_version: source_code_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#source_code_version ApprunnerService#source_code_version}
        :param code_configuration: code_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#code_configuration ApprunnerService#code_configuration}
        '''
        value = ApprunnerServiceSourceConfigurationCodeRepository(
            repository_url=repository_url,
            source_code_version=source_code_version,
            code_configuration=code_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putCodeRepository", [value]))

    @jsii.member(jsii_name="putImageRepository")
    def put_image_repository(
        self,
        *,
        image_identifier: builtins.str,
        image_repository_type: builtins.str,
        image_configuration: typing.Optional[ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration] = None,
    ) -> None:
        '''
        :param image_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_identifier ApprunnerService#image_identifier}.
        :param image_repository_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_repository_type ApprunnerService#image_repository_type}.
        :param image_configuration: image_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_service#image_configuration ApprunnerService#image_configuration}
        '''
        value = ApprunnerServiceSourceConfigurationImageRepository(
            image_identifier=image_identifier,
            image_repository_type=image_repository_type,
            image_configuration=image_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putImageRepository", [value]))

    @jsii.member(jsii_name="resetAuthenticationConfiguration")
    def reset_authentication_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationConfiguration", []))

    @jsii.member(jsii_name="resetAutoDeploymentsEnabled")
    def reset_auto_deployments_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeploymentsEnabled", []))

    @jsii.member(jsii_name="resetCodeRepository")
    def reset_code_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeRepository", []))

    @jsii.member(jsii_name="resetImageRepository")
    def reset_image_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageRepository", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> ApprunnerServiceSourceConfigurationAuthenticationConfigurationOutputReference:
        return typing.cast(ApprunnerServiceSourceConfigurationAuthenticationConfigurationOutputReference, jsii.get(self, "authenticationConfiguration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeRepository")
    def code_repository(
        self,
    ) -> ApprunnerServiceSourceConfigurationCodeRepositoryOutputReference:
        return typing.cast(ApprunnerServiceSourceConfigurationCodeRepositoryOutputReference, jsii.get(self, "codeRepository"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRepository")
    def image_repository(
        self,
    ) -> ApprunnerServiceSourceConfigurationImageRepositoryOutputReference:
        return typing.cast(ApprunnerServiceSourceConfigurationImageRepositoryOutputReference, jsii.get(self, "imageRepository"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authenticationConfigurationInput")
    def authentication_configuration_input(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationAuthenticationConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationAuthenticationConfiguration], jsii.get(self, "authenticationConfigurationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoDeploymentsEnabledInput")
    def auto_deployments_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoDeploymentsEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeRepositoryInput")
    def code_repository_input(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationCodeRepository]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationCodeRepository], jsii.get(self, "codeRepositoryInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRepositoryInput")
    def image_repository_input(
        self,
    ) -> typing.Optional[ApprunnerServiceSourceConfigurationImageRepository]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfigurationImageRepository], jsii.get(self, "imageRepositoryInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoDeploymentsEnabled")
    def auto_deployments_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoDeploymentsEnabled"))

    @auto_deployments_enabled.setter
    def auto_deployments_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "autoDeploymentsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApprunnerServiceSourceConfiguration]:
        return typing.cast(typing.Optional[ApprunnerServiceSourceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApprunnerServiceSourceConfiguration],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ApprunnerVpcConnector(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerVpcConnector",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector aws_apprunner_vpc_connector}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        security_groups: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
        vpc_connector_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector aws_apprunner_vpc_connector} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#security_groups ApprunnerVpcConnector#security_groups}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#subnets ApprunnerVpcConnector#subnets}.
        :param vpc_connector_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#vpc_connector_name ApprunnerVpcConnector#vpc_connector_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#id ApprunnerVpcConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#tags ApprunnerVpcConnector#tags}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ApprunnerVpcConnectorConfig(
            security_groups=security_groups,
            subnets=subnets,
            vpc_connector_name=vpc_connector_name,
            id=id,
            tags=tags,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectorRevision")
    def vpc_connector_revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vpcConnectorRevision"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectorNameInput")
    def vpc_connector_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcConnectorNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "securityGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectorName")
    def vpc_connector_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcConnectorName"))

    @vpc_connector_name.setter
    def vpc_connector_name(self, value: builtins.str) -> None:
        jsii.set(self, "vpcConnectorName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apprunner.ApprunnerVpcConnectorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "security_groups": "securityGroups",
        "subnets": "subnets",
        "vpc_connector_name": "vpcConnectorName",
        "id": "id",
        "tags": "tags",
    },
)
class ApprunnerVpcConnectorConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        security_groups: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
        vpc_connector_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''App Runner.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#security_groups ApprunnerVpcConnector#security_groups}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#subnets ApprunnerVpcConnector#subnets}.
        :param vpc_connector_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#vpc_connector_name ApprunnerVpcConnector#vpc_connector_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#id ApprunnerVpcConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#tags ApprunnerVpcConnector#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "security_groups": security_groups,
            "subnets": subnets,
            "vpc_connector_name": vpc_connector_name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#security_groups ApprunnerVpcConnector#security_groups}.'''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#subnets ApprunnerVpcConnector#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_connector_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#vpc_connector_name ApprunnerVpcConnector#vpc_connector_name}.'''
        result = self._values.get("vpc_connector_name")
        assert result is not None, "Required property 'vpc_connector_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#id ApprunnerVpcConnector#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apprunner_vpc_connector#tags ApprunnerVpcConnector#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprunnerVpcConnectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApprunnerAutoScalingConfigurationVersion",
    "ApprunnerAutoScalingConfigurationVersionConfig",
    "ApprunnerConnection",
    "ApprunnerConnectionConfig",
    "ApprunnerCustomDomainAssociation",
    "ApprunnerCustomDomainAssociationCertificateValidationRecords",
    "ApprunnerCustomDomainAssociationCertificateValidationRecordsList",
    "ApprunnerCustomDomainAssociationCertificateValidationRecordsOutputReference",
    "ApprunnerCustomDomainAssociationConfig",
    "ApprunnerObservabilityConfiguration",
    "ApprunnerObservabilityConfigurationConfig",
    "ApprunnerObservabilityConfigurationTraceConfiguration",
    "ApprunnerObservabilityConfigurationTraceConfigurationOutputReference",
    "ApprunnerService",
    "ApprunnerServiceConfig",
    "ApprunnerServiceEncryptionConfiguration",
    "ApprunnerServiceEncryptionConfigurationOutputReference",
    "ApprunnerServiceHealthCheckConfiguration",
    "ApprunnerServiceHealthCheckConfigurationOutputReference",
    "ApprunnerServiceInstanceConfiguration",
    "ApprunnerServiceInstanceConfigurationOutputReference",
    "ApprunnerServiceNetworkConfiguration",
    "ApprunnerServiceNetworkConfigurationEgressConfiguration",
    "ApprunnerServiceNetworkConfigurationEgressConfigurationOutputReference",
    "ApprunnerServiceNetworkConfigurationOutputReference",
    "ApprunnerServiceObservabilityConfiguration",
    "ApprunnerServiceObservabilityConfigurationOutputReference",
    "ApprunnerServiceSourceConfiguration",
    "ApprunnerServiceSourceConfigurationAuthenticationConfiguration",
    "ApprunnerServiceSourceConfigurationAuthenticationConfigurationOutputReference",
    "ApprunnerServiceSourceConfigurationCodeRepository",
    "ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfiguration",
    "ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues",
    "ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesOutputReference",
    "ApprunnerServiceSourceConfigurationCodeRepositoryCodeConfigurationOutputReference",
    "ApprunnerServiceSourceConfigurationCodeRepositoryOutputReference",
    "ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersion",
    "ApprunnerServiceSourceConfigurationCodeRepositorySourceCodeVersionOutputReference",
    "ApprunnerServiceSourceConfigurationImageRepository",
    "ApprunnerServiceSourceConfigurationImageRepositoryImageConfiguration",
    "ApprunnerServiceSourceConfigurationImageRepositoryImageConfigurationOutputReference",
    "ApprunnerServiceSourceConfigurationImageRepositoryOutputReference",
    "ApprunnerServiceSourceConfigurationOutputReference",
    "ApprunnerVpcConnector",
    "ApprunnerVpcConnectorConfig",
]

publication.publish()
