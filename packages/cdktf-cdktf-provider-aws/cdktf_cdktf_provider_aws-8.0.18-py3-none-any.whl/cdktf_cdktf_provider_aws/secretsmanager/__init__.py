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


class DataAwsSecretsmanagerRandomPassword(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerRandomPassword",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password aws_secretsmanager_random_password}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        exclude_characters: typing.Optional[builtins.str] = None,
        exclude_lowercase: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude_numbers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude_punctuation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude_uppercase: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        include_space: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_length: typing.Optional[jsii.Number] = None,
        random_password: typing.Optional[builtins.str] = None,
        require_each_included_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password aws_secretsmanager_random_password} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param exclude_characters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_characters DataAwsSecretsmanagerRandomPassword#exclude_characters}.
        :param exclude_lowercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_lowercase DataAwsSecretsmanagerRandomPassword#exclude_lowercase}.
        :param exclude_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_numbers DataAwsSecretsmanagerRandomPassword#exclude_numbers}.
        :param exclude_punctuation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_punctuation DataAwsSecretsmanagerRandomPassword#exclude_punctuation}.
        :param exclude_uppercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_uppercase DataAwsSecretsmanagerRandomPassword#exclude_uppercase}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#id DataAwsSecretsmanagerRandomPassword#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#include_space DataAwsSecretsmanagerRandomPassword#include_space}.
        :param password_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#password_length DataAwsSecretsmanagerRandomPassword#password_length}.
        :param random_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#random_password DataAwsSecretsmanagerRandomPassword#random_password}.
        :param require_each_included_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#require_each_included_type DataAwsSecretsmanagerRandomPassword#require_each_included_type}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsSecretsmanagerRandomPasswordConfig(
            exclude_characters=exclude_characters,
            exclude_lowercase=exclude_lowercase,
            exclude_numbers=exclude_numbers,
            exclude_punctuation=exclude_punctuation,
            exclude_uppercase=exclude_uppercase,
            id=id,
            include_space=include_space,
            password_length=password_length,
            random_password=random_password,
            require_each_included_type=require_each_included_type,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetExcludeCharacters")
    def reset_exclude_characters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeCharacters", []))

    @jsii.member(jsii_name="resetExcludeLowercase")
    def reset_exclude_lowercase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeLowercase", []))

    @jsii.member(jsii_name="resetExcludeNumbers")
    def reset_exclude_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeNumbers", []))

    @jsii.member(jsii_name="resetExcludePunctuation")
    def reset_exclude_punctuation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludePunctuation", []))

    @jsii.member(jsii_name="resetExcludeUppercase")
    def reset_exclude_uppercase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeUppercase", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncludeSpace")
    def reset_include_space(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSpace", []))

    @jsii.member(jsii_name="resetPasswordLength")
    def reset_password_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordLength", []))

    @jsii.member(jsii_name="resetRandomPassword")
    def reset_random_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRandomPassword", []))

    @jsii.member(jsii_name="resetRequireEachIncludedType")
    def reset_require_each_included_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireEachIncludedType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeCharactersInput")
    def exclude_characters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "excludeCharactersInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeLowercaseInput")
    def exclude_lowercase_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludeLowercaseInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeNumbersInput")
    def exclude_numbers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludeNumbersInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludePunctuationInput")
    def exclude_punctuation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludePunctuationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeUppercaseInput")
    def exclude_uppercase_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludeUppercaseInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="includeSpaceInput")
    def include_space_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeSpaceInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="passwordLengthInput")
    def password_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordLengthInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="randomPasswordInput")
    def random_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "randomPasswordInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="requireEachIncludedTypeInput")
    def require_each_included_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireEachIncludedTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeCharacters")
    def exclude_characters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "excludeCharacters"))

    @exclude_characters.setter
    def exclude_characters(self, value: builtins.str) -> None:
        jsii.set(self, "excludeCharacters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeLowercase")
    def exclude_lowercase(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludeLowercase"))

    @exclude_lowercase.setter
    def exclude_lowercase(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "excludeLowercase", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeNumbers")
    def exclude_numbers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludeNumbers"))

    @exclude_numbers.setter
    def exclude_numbers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "excludeNumbers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludePunctuation")
    def exclude_punctuation(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludePunctuation"))

    @exclude_punctuation.setter
    def exclude_punctuation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "excludePunctuation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeUppercase")
    def exclude_uppercase(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludeUppercase"))

    @exclude_uppercase.setter
    def exclude_uppercase(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "excludeUppercase", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="includeSpace")
    def include_space(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeSpace"))

    @include_space.setter
    def include_space(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "includeSpace", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="passwordLength")
    def password_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordLength"))

    @password_length.setter
    def password_length(self, value: jsii.Number) -> None:
        jsii.set(self, "passwordLength", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="randomPassword")
    def random_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "randomPassword"))

    @random_password.setter
    def random_password(self, value: builtins.str) -> None:
        jsii.set(self, "randomPassword", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="requireEachIncludedType")
    def require_each_included_type(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireEachIncludedType"))

    @require_each_included_type.setter
    def require_each_included_type(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "requireEachIncludedType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerRandomPasswordConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "exclude_characters": "excludeCharacters",
        "exclude_lowercase": "excludeLowercase",
        "exclude_numbers": "excludeNumbers",
        "exclude_punctuation": "excludePunctuation",
        "exclude_uppercase": "excludeUppercase",
        "id": "id",
        "include_space": "includeSpace",
        "password_length": "passwordLength",
        "random_password": "randomPassword",
        "require_each_included_type": "requireEachIncludedType",
    },
)
class DataAwsSecretsmanagerRandomPasswordConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        exclude_characters: typing.Optional[builtins.str] = None,
        exclude_lowercase: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude_numbers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude_punctuation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude_uppercase: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        include_space: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_length: typing.Optional[jsii.Number] = None,
        random_password: typing.Optional[builtins.str] = None,
        require_each_included_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param exclude_characters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_characters DataAwsSecretsmanagerRandomPassword#exclude_characters}.
        :param exclude_lowercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_lowercase DataAwsSecretsmanagerRandomPassword#exclude_lowercase}.
        :param exclude_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_numbers DataAwsSecretsmanagerRandomPassword#exclude_numbers}.
        :param exclude_punctuation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_punctuation DataAwsSecretsmanagerRandomPassword#exclude_punctuation}.
        :param exclude_uppercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_uppercase DataAwsSecretsmanagerRandomPassword#exclude_uppercase}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#id DataAwsSecretsmanagerRandomPassword#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#include_space DataAwsSecretsmanagerRandomPassword#include_space}.
        :param password_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#password_length DataAwsSecretsmanagerRandomPassword#password_length}.
        :param random_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#random_password DataAwsSecretsmanagerRandomPassword#random_password}.
        :param require_each_included_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#require_each_included_type DataAwsSecretsmanagerRandomPassword#require_each_included_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if exclude_characters is not None:
            self._values["exclude_characters"] = exclude_characters
        if exclude_lowercase is not None:
            self._values["exclude_lowercase"] = exclude_lowercase
        if exclude_numbers is not None:
            self._values["exclude_numbers"] = exclude_numbers
        if exclude_punctuation is not None:
            self._values["exclude_punctuation"] = exclude_punctuation
        if exclude_uppercase is not None:
            self._values["exclude_uppercase"] = exclude_uppercase
        if id is not None:
            self._values["id"] = id
        if include_space is not None:
            self._values["include_space"] = include_space
        if password_length is not None:
            self._values["password_length"] = password_length
        if random_password is not None:
            self._values["random_password"] = random_password
        if require_each_included_type is not None:
            self._values["require_each_included_type"] = require_each_included_type

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
    def exclude_characters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_characters DataAwsSecretsmanagerRandomPassword#exclude_characters}.'''
        result = self._values.get("exclude_characters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_lowercase(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_lowercase DataAwsSecretsmanagerRandomPassword#exclude_lowercase}.'''
        result = self._values.get("exclude_lowercase")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exclude_numbers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_numbers DataAwsSecretsmanagerRandomPassword#exclude_numbers}.'''
        result = self._values.get("exclude_numbers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exclude_punctuation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_punctuation DataAwsSecretsmanagerRandomPassword#exclude_punctuation}.'''
        result = self._values.get("exclude_punctuation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exclude_uppercase(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#exclude_uppercase DataAwsSecretsmanagerRandomPassword#exclude_uppercase}.'''
        result = self._values.get("exclude_uppercase")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#id DataAwsSecretsmanagerRandomPassword#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_space(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#include_space DataAwsSecretsmanagerRandomPassword#include_space}.'''
        result = self._values.get("include_space")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#password_length DataAwsSecretsmanagerRandomPassword#password_length}.'''
        result = self._values.get("password_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def random_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#random_password DataAwsSecretsmanagerRandomPassword#random_password}.'''
        result = self._values.get("random_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_each_included_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_random_password#require_each_included_type DataAwsSecretsmanagerRandomPassword#require_each_included_type}.'''
        result = self._values.get("require_each_included_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSecretsmanagerRandomPasswordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSecretsmanagerSecret(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecret",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret aws_secretsmanager_secret}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret aws_secretsmanager_secret} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#arn DataAwsSecretsmanagerSecret#arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#id DataAwsSecretsmanagerSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#name DataAwsSecretsmanagerSecret#name}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsSecretsmanagerSecretConfig(
            arn=arn,
            id=id,
            name=name,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationEnabled")
    def rotation_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "rotationEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationLambdaArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationRules")
    def rotation_rules(self) -> "DataAwsSecretsmanagerSecretRotationRulesList":
        return typing.cast("DataAwsSecretsmanagerSecretRotationRulesList", jsii.get(self, "rotationRules"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        jsii.set(self, "arn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "arn": "arn",
        "id": "id",
        "name": "name",
    },
)
class DataAwsSecretsmanagerSecretConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#arn DataAwsSecretsmanagerSecret#arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#id DataAwsSecretsmanagerSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#name DataAwsSecretsmanagerSecret#name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if arn is not None:
            self._values["arn"] = arn
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

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
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#arn DataAwsSecretsmanagerSecret#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#id DataAwsSecretsmanagerSecret#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret#name DataAwsSecretsmanagerSecret#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSecretsmanagerSecretConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSecretsmanagerSecretRotation(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation aws_secretsmanager_secret_rotation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation aws_secretsmanager_secret_rotation} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation#secret_id DataAwsSecretsmanagerSecretRotation#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation#id DataAwsSecretsmanagerSecretRotation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsSecretsmanagerSecretRotationConfig(
            secret_id=secret_id,
            id=id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

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
    @jsii.member(jsii_name="rotationEnabled")
    def rotation_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "rotationEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationLambdaArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationRules")
    def rotation_rules(self) -> "DataAwsSecretsmanagerSecretRotationRotationRulesList":
        return typing.cast("DataAwsSecretsmanagerSecretRotationRotationRulesList", jsii.get(self, "rotationRules"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        jsii.set(self, "secretId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "secret_id": "secretId",
        "id": "id",
    },
)
class DataAwsSecretsmanagerSecretRotationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation#secret_id DataAwsSecretsmanagerSecretRotation#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation#id DataAwsSecretsmanagerSecretRotation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "secret_id": secret_id,
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
    def secret_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation#secret_id DataAwsSecretsmanagerSecretRotation#secret_id}.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_rotation#id DataAwsSecretsmanagerSecretRotation#id}.

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
        return "DataAwsSecretsmanagerSecretRotationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationRotationRules",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsSecretsmanagerSecretRotationRotationRules:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSecretsmanagerSecretRotationRotationRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSecretsmanagerSecretRotationRotationRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationRotationRulesList",
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
    ) -> "DataAwsSecretsmanagerSecretRotationRotationRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        return typing.cast("DataAwsSecretsmanagerSecretRotationRotationRulesOutputReference", jsii.invoke(self, "get", [index]))

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


class DataAwsSecretsmanagerSecretRotationRotationRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationRotationRulesOutputReference",
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
    @jsii.member(jsii_name="automaticallyAfterDays")
    def automatically_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automaticallyAfterDays"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsSecretsmanagerSecretRotationRotationRules]:
        return typing.cast(typing.Optional[DataAwsSecretsmanagerSecretRotationRotationRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsSecretsmanagerSecretRotationRotationRules],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationRules",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsSecretsmanagerSecretRotationRules:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSecretsmanagerSecretRotationRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSecretsmanagerSecretRotationRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationRulesList",
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
    ) -> "DataAwsSecretsmanagerSecretRotationRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        return typing.cast("DataAwsSecretsmanagerSecretRotationRulesOutputReference", jsii.invoke(self, "get", [index]))

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


class DataAwsSecretsmanagerSecretRotationRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretRotationRulesOutputReference",
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
    @jsii.member(jsii_name="automaticallyAfterDays")
    def automatically_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automaticallyAfterDays"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsSecretsmanagerSecretRotationRules]:
        return typing.cast(typing.Optional[DataAwsSecretsmanagerSecretRotationRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsSecretsmanagerSecretRotationRules],
    ) -> None:
        jsii.set(self, "internalValue", value)


class DataAwsSecretsmanagerSecretVersion(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretVersion",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version aws_secretsmanager_secret_version}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
        version_stage: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version aws_secretsmanager_secret_version} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#secret_id DataAwsSecretsmanagerSecretVersion#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#id DataAwsSecretsmanagerSecretVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#version_id DataAwsSecretsmanagerSecretVersion#version_id}.
        :param version_stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#version_stage DataAwsSecretsmanagerSecretVersion#version_stage}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsSecretsmanagerSecretVersionConfig(
            secret_id=secret_id,
            id=id,
            version_id=version_id,
            version_stage=version_stage,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetVersionId")
    def reset_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionId", []))

    @jsii.member(jsii_name="resetVersionStage")
    def reset_version_stage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionStage", []))

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
    @jsii.member(jsii_name="secretBinary")
    def secret_binary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretBinary"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretString")
    def secret_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretString"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionStages")
    def version_stages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "versionStages"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionStageInput")
    def version_stage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionStageInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        jsii.set(self, "secretId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        jsii.set(self, "versionId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionStage")
    def version_stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionStage"))

    @version_stage.setter
    def version_stage(self, value: builtins.str) -> None:
        jsii.set(self, "versionStage", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretVersionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "secret_id": "secretId",
        "id": "id",
        "version_id": "versionId",
        "version_stage": "versionStage",
    },
)
class DataAwsSecretsmanagerSecretVersionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
        version_stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#secret_id DataAwsSecretsmanagerSecretVersion#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#id DataAwsSecretsmanagerSecretVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#version_id DataAwsSecretsmanagerSecretVersion#version_id}.
        :param version_stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#version_stage DataAwsSecretsmanagerSecretVersion#version_stage}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "secret_id": secret_id,
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
        if version_id is not None:
            self._values["version_id"] = version_id
        if version_stage is not None:
            self._values["version_stage"] = version_stage

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
    def secret_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#secret_id DataAwsSecretsmanagerSecretVersion#secret_id}.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#id DataAwsSecretsmanagerSecretVersion#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#version_id DataAwsSecretsmanagerSecretVersion#version_id}.'''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_stage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version#version_stage DataAwsSecretsmanagerSecretVersion#version_stage}.'''
        result = self._values.get("version_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSecretsmanagerSecretVersionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSecretsmanagerSecrets(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecrets",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets aws_secretsmanager_secrets}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["DataAwsSecretsmanagerSecretsFilter"]]] = None,
        id: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets aws_secretsmanager_secrets} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#filter DataAwsSecretsmanagerSecrets#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#id DataAwsSecretsmanagerSecrets#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsSecretsmanagerSecretsConfig(
            filter=filter,
            id=id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence["DataAwsSecretsmanagerSecretsFilter"]],
    ) -> None:
        '''
        :param value: -
        '''
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

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
    @jsii.member(jsii_name="arns")
    def arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "arns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsSecretsmanagerSecretsFilterList":
        return typing.cast("DataAwsSecretsmanagerSecretsFilterList", jsii.get(self, "filter"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="names")
    def names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "names"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSecretsmanagerSecretsFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSecretsmanagerSecretsFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "filter": "filter",
        "id": "id",
    },
)
class DataAwsSecretsmanagerSecretsConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["DataAwsSecretsmanagerSecretsFilter"]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#filter DataAwsSecretsmanagerSecrets#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#id DataAwsSecretsmanagerSecrets#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if filter is not None:
            self._values["filter"] = filter
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
    def filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSecretsmanagerSecretsFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#filter DataAwsSecretsmanagerSecrets#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSecretsmanagerSecretsFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#id DataAwsSecretsmanagerSecrets#id}.

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
        return "DataAwsSecretsmanagerSecretsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretsFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class DataAwsSecretsmanagerSecretsFilter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#name DataAwsSecretsmanagerSecrets#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#values DataAwsSecretsmanagerSecrets#values}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#name DataAwsSecretsmanagerSecrets#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/secretsmanager_secrets#values DataAwsSecretsmanagerSecrets#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSecretsmanagerSecretsFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSecretsmanagerSecretsFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretsFilterList",
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
    ) -> "DataAwsSecretsmanagerSecretsFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        return typing.cast("DataAwsSecretsmanagerSecretsFilterOutputReference", jsii.invoke(self, "get", [index]))

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

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSecretsmanagerSecretsFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSecretsmanagerSecretsFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSecretsmanagerSecretsFilter]]],
    ) -> None:
        jsii.set(self, "internalValue", value)


class DataAwsSecretsmanagerSecretsFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.DataAwsSecretsmanagerSecretsFilterOutputReference",
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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "values", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsSecretsmanagerSecretsFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsSecretsmanagerSecretsFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsSecretsmanagerSecretsFilter, cdktf.IResolvable]],
    ) -> None:
        jsii.set(self, "internalValue", value)


class SecretsmanagerSecret(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecret",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret aws_secretsmanager_secret}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        force_overwrite_replica_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        recovery_window_in_days: typing.Optional[jsii.Number] = None,
        replica: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["SecretsmanagerSecretReplica"]]] = None,
        rotation_lambda_arn: typing.Optional[builtins.str] = None,
        rotation_rules: typing.Optional["SecretsmanagerSecretRotationRules"] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret aws_secretsmanager_secret} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#description SecretsmanagerSecret#description}.
        :param force_overwrite_replica_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#force_overwrite_replica_secret SecretsmanagerSecret#force_overwrite_replica_secret}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#id SecretsmanagerSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#kms_key_id SecretsmanagerSecret#kms_key_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#name SecretsmanagerSecret#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#name_prefix SecretsmanagerSecret#name_prefix}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#policy SecretsmanagerSecret#policy}.
        :param recovery_window_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#recovery_window_in_days SecretsmanagerSecret#recovery_window_in_days}.
        :param replica: replica block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#replica SecretsmanagerSecret#replica}
        :param rotation_lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#rotation_lambda_arn SecretsmanagerSecret#rotation_lambda_arn}.
        :param rotation_rules: rotation_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#rotation_rules SecretsmanagerSecret#rotation_rules}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#tags SecretsmanagerSecret#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#tags_all SecretsmanagerSecret#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = SecretsmanagerSecretConfig(
            description=description,
            force_overwrite_replica_secret=force_overwrite_replica_secret,
            id=id,
            kms_key_id=kms_key_id,
            name=name,
            name_prefix=name_prefix,
            policy=policy,
            recovery_window_in_days=recovery_window_in_days,
            replica=replica,
            rotation_lambda_arn=rotation_lambda_arn,
            rotation_rules=rotation_rules,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putReplica")
    def put_replica(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence["SecretsmanagerSecretReplica"]],
    ) -> None:
        '''
        :param value: -
        '''
        return typing.cast(None, jsii.invoke(self, "putReplica", [value]))

    @jsii.member(jsii_name="putRotationRules")
    def put_rotation_rules(self, *, automatically_after_days: jsii.Number) -> None:
        '''
        :param automatically_after_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#automatically_after_days SecretsmanagerSecret#automatically_after_days}.
        '''
        value = SecretsmanagerSecretRotationRules(
            automatically_after_days=automatically_after_days
        )

        return typing.cast(None, jsii.invoke(self, "putRotationRules", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetForceOverwriteReplicaSecret")
    def reset_force_overwrite_replica_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceOverwriteReplicaSecret", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetRecoveryWindowInDays")
    def reset_recovery_window_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryWindowInDays", []))

    @jsii.member(jsii_name="resetReplica")
    def reset_replica(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplica", []))

    @jsii.member(jsii_name="resetRotationLambdaArn")
    def reset_rotation_lambda_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationLambdaArn", []))

    @jsii.member(jsii_name="resetRotationRules")
    def reset_rotation_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationRules", []))

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
    @jsii.member(jsii_name="replica")
    def replica(self) -> "SecretsmanagerSecretReplicaList":
        return typing.cast("SecretsmanagerSecretReplicaList", jsii.get(self, "replica"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationEnabled")
    def rotation_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "rotationEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationRules")
    def rotation_rules(self) -> "SecretsmanagerSecretRotationRulesOutputReference":
        return typing.cast("SecretsmanagerSecretRotationRulesOutputReference", jsii.get(self, "rotationRules"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="forceOverwriteReplicaSecretInput")
    def force_overwrite_replica_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceOverwriteReplicaSecretInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recoveryWindowInDaysInput")
    def recovery_window_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recoveryWindowInDaysInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicaInput")
    def replica_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecretsmanagerSecretReplica"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecretsmanagerSecretReplica"]]], jsii.get(self, "replicaInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationLambdaArnInput")
    def rotation_lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rotationLambdaArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationRulesInput")
    def rotation_rules_input(
        self,
    ) -> typing.Optional["SecretsmanagerSecretRotationRules"]:
        return typing.cast(typing.Optional["SecretsmanagerSecretRotationRules"], jsii.get(self, "rotationRulesInput"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="forceOverwriteReplicaSecret")
    def force_overwrite_replica_secret(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceOverwriteReplicaSecret"))

    @force_overwrite_replica_secret.setter
    def force_overwrite_replica_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "forceOverwriteReplicaSecret", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        jsii.set(self, "namePrefix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        jsii.set(self, "policy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recoveryWindowInDays")
    def recovery_window_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "recoveryWindowInDays"))

    @recovery_window_in_days.setter
    def recovery_window_in_days(self, value: jsii.Number) -> None:
        jsii.set(self, "recoveryWindowInDays", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationLambdaArn"))

    @rotation_lambda_arn.setter
    def rotation_lambda_arn(self, value: builtins.str) -> None:
        jsii.set(self, "rotationLambdaArn", value)

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
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "description": "description",
        "force_overwrite_replica_secret": "forceOverwriteReplicaSecret",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "name": "name",
        "name_prefix": "namePrefix",
        "policy": "policy",
        "recovery_window_in_days": "recoveryWindowInDays",
        "replica": "replica",
        "rotation_lambda_arn": "rotationLambdaArn",
        "rotation_rules": "rotationRules",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SecretsmanagerSecretConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        description: typing.Optional[builtins.str] = None,
        force_overwrite_replica_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        recovery_window_in_days: typing.Optional[jsii.Number] = None,
        replica: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["SecretsmanagerSecretReplica"]]] = None,
        rotation_lambda_arn: typing.Optional[builtins.str] = None,
        rotation_rules: typing.Optional["SecretsmanagerSecretRotationRules"] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#description SecretsmanagerSecret#description}.
        :param force_overwrite_replica_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#force_overwrite_replica_secret SecretsmanagerSecret#force_overwrite_replica_secret}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#id SecretsmanagerSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#kms_key_id SecretsmanagerSecret#kms_key_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#name SecretsmanagerSecret#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#name_prefix SecretsmanagerSecret#name_prefix}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#policy SecretsmanagerSecret#policy}.
        :param recovery_window_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#recovery_window_in_days SecretsmanagerSecret#recovery_window_in_days}.
        :param replica: replica block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#replica SecretsmanagerSecret#replica}
        :param rotation_lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#rotation_lambda_arn SecretsmanagerSecret#rotation_lambda_arn}.
        :param rotation_rules: rotation_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#rotation_rules SecretsmanagerSecret#rotation_rules}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#tags SecretsmanagerSecret#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#tags_all SecretsmanagerSecret#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(rotation_rules, dict):
            rotation_rules = SecretsmanagerSecretRotationRules(**rotation_rules)
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if description is not None:
            self._values["description"] = description
        if force_overwrite_replica_secret is not None:
            self._values["force_overwrite_replica_secret"] = force_overwrite_replica_secret
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if policy is not None:
            self._values["policy"] = policy
        if recovery_window_in_days is not None:
            self._values["recovery_window_in_days"] = recovery_window_in_days
        if replica is not None:
            self._values["replica"] = replica
        if rotation_lambda_arn is not None:
            self._values["rotation_lambda_arn"] = rotation_lambda_arn
        if rotation_rules is not None:
            self._values["rotation_rules"] = rotation_rules
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
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#description SecretsmanagerSecret#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_overwrite_replica_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#force_overwrite_replica_secret SecretsmanagerSecret#force_overwrite_replica_secret}.'''
        result = self._values.get("force_overwrite_replica_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#id SecretsmanagerSecret#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#kms_key_id SecretsmanagerSecret#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#name SecretsmanagerSecret#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#name_prefix SecretsmanagerSecret#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#policy SecretsmanagerSecret#policy}.'''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_window_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#recovery_window_in_days SecretsmanagerSecret#recovery_window_in_days}.'''
        result = self._values.get("recovery_window_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replica(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecretsmanagerSecretReplica"]]]:
        '''replica block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#replica SecretsmanagerSecret#replica}
        '''
        result = self._values.get("replica")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecretsmanagerSecretReplica"]]], result)

    @builtins.property
    def rotation_lambda_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#rotation_lambda_arn SecretsmanagerSecret#rotation_lambda_arn}.'''
        result = self._values.get("rotation_lambda_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotation_rules(self) -> typing.Optional["SecretsmanagerSecretRotationRules"]:
        '''rotation_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#rotation_rules SecretsmanagerSecret#rotation_rules}
        '''
        result = self._values.get("rotation_rules")
        return typing.cast(typing.Optional["SecretsmanagerSecretRotationRules"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#tags SecretsmanagerSecret#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#tags_all SecretsmanagerSecret#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsmanagerSecretConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretsmanagerSecretPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy aws_secretsmanager_secret_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        policy: builtins.str,
        secret_arn: builtins.str,
        block_public_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy aws_secretsmanager_secret_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#policy SecretsmanagerSecretPolicy#policy}.
        :param secret_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#secret_arn SecretsmanagerSecretPolicy#secret_arn}.
        :param block_public_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#block_public_policy SecretsmanagerSecretPolicy#block_public_policy}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#id SecretsmanagerSecretPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = SecretsmanagerSecretPolicyConfig(
            policy=policy,
            secret_arn=secret_arn,
            block_public_policy=block_public_policy,
            id=id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBlockPublicPolicy")
    def reset_block_public_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockPublicPolicy", []))

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
    @jsii.member(jsii_name="blockPublicPolicyInput")
    def block_public_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockPublicPolicyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretArnInput")
    def secret_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockPublicPolicy")
    def block_public_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blockPublicPolicy"))

    @block_public_policy.setter
    def block_public_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "blockPublicPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        jsii.set(self, "policy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretArn")
    def secret_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretArn"))

    @secret_arn.setter
    def secret_arn(self, value: builtins.str) -> None:
        jsii.set(self, "secretArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "policy": "policy",
        "secret_arn": "secretArn",
        "block_public_policy": "blockPublicPolicy",
        "id": "id",
    },
)
class SecretsmanagerSecretPolicyConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        policy: builtins.str,
        secret_arn: builtins.str,
        block_public_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#policy SecretsmanagerSecretPolicy#policy}.
        :param secret_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#secret_arn SecretsmanagerSecretPolicy#secret_arn}.
        :param block_public_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#block_public_policy SecretsmanagerSecretPolicy#block_public_policy}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#id SecretsmanagerSecretPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "policy": policy,
            "secret_arn": secret_arn,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if block_public_policy is not None:
            self._values["block_public_policy"] = block_public_policy
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
    def policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#policy SecretsmanagerSecretPolicy#policy}.'''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#secret_arn SecretsmanagerSecretPolicy#secret_arn}.'''
        result = self._values.get("secret_arn")
        assert result is not None, "Required property 'secret_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def block_public_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#block_public_policy SecretsmanagerSecretPolicy#block_public_policy}.'''
        result = self._values.get("block_public_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_policy#id SecretsmanagerSecretPolicy#id}.

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
        return "SecretsmanagerSecretPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretReplica",
    jsii_struct_bases=[],
    name_mapping={"region": "region", "kms_key_id": "kmsKeyId"},
)
class SecretsmanagerSecretReplica:
    def __init__(
        self,
        *,
        region: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#region SecretsmanagerSecret#region}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#kms_key_id SecretsmanagerSecret#kms_key_id}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "region": region,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#region SecretsmanagerSecret#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#kms_key_id SecretsmanagerSecret#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsmanagerSecretReplica(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretsmanagerSecretReplicaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretReplicaList",
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
    def get(self, index: jsii.Number) -> "SecretsmanagerSecretReplicaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        return typing.cast("SecretsmanagerSecretReplicaOutputReference", jsii.invoke(self, "get", [index]))

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

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecretsmanagerSecretReplica]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecretsmanagerSecretReplica]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecretsmanagerSecretReplica]]],
    ) -> None:
        jsii.set(self, "internalValue", value)


class SecretsmanagerSecretReplicaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretReplicaOutputReference",
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

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lastAccessedDate")
    def last_accessed_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastAccessedDate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="statusMessage")
    def status_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        jsii.set(self, "region", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecretsmanagerSecretReplica, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecretsmanagerSecretReplica, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecretsmanagerSecretReplica, cdktf.IResolvable]],
    ) -> None:
        jsii.set(self, "internalValue", value)


class SecretsmanagerSecretRotation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretRotation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation aws_secretsmanager_secret_rotation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        rotation_lambda_arn: builtins.str,
        rotation_rules: "SecretsmanagerSecretRotationRotationRules",
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation aws_secretsmanager_secret_rotation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param rotation_lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#rotation_lambda_arn SecretsmanagerSecretRotation#rotation_lambda_arn}.
        :param rotation_rules: rotation_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#rotation_rules SecretsmanagerSecretRotation#rotation_rules}
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#secret_id SecretsmanagerSecretRotation#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#id SecretsmanagerSecretRotation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#tags SecretsmanagerSecretRotation#tags}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = SecretsmanagerSecretRotationConfig(
            rotation_lambda_arn=rotation_lambda_arn,
            rotation_rules=rotation_rules,
            secret_id=secret_id,
            id=id,
            tags=tags,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRotationRules")
    def put_rotation_rules(self, *, automatically_after_days: jsii.Number) -> None:
        '''
        :param automatically_after_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#automatically_after_days SecretsmanagerSecretRotation#automatically_after_days}.
        '''
        value = SecretsmanagerSecretRotationRotationRules(
            automatically_after_days=automatically_after_days
        )

        return typing.cast(None, jsii.invoke(self, "putRotationRules", [value]))

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
    @jsii.member(jsii_name="rotationEnabled")
    def rotation_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "rotationEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationRules")
    def rotation_rules(
        self,
    ) -> "SecretsmanagerSecretRotationRotationRulesOutputReference":
        return typing.cast("SecretsmanagerSecretRotationRotationRulesOutputReference", jsii.get(self, "rotationRules"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationLambdaArnInput")
    def rotation_lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rotationLambdaArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationRulesInput")
    def rotation_rules_input(
        self,
    ) -> typing.Optional["SecretsmanagerSecretRotationRotationRules"]:
        return typing.cast(typing.Optional["SecretsmanagerSecretRotationRotationRules"], jsii.get(self, "rotationRulesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationLambdaArn"))

    @rotation_lambda_arn.setter
    def rotation_lambda_arn(self, value: builtins.str) -> None:
        jsii.set(self, "rotationLambdaArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        jsii.set(self, "secretId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretRotationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "rotation_lambda_arn": "rotationLambdaArn",
        "rotation_rules": "rotationRules",
        "secret_id": "secretId",
        "id": "id",
        "tags": "tags",
    },
)
class SecretsmanagerSecretRotationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        rotation_lambda_arn: builtins.str,
        rotation_rules: "SecretsmanagerSecretRotationRotationRules",
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param rotation_lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#rotation_lambda_arn SecretsmanagerSecretRotation#rotation_lambda_arn}.
        :param rotation_rules: rotation_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#rotation_rules SecretsmanagerSecretRotation#rotation_rules}
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#secret_id SecretsmanagerSecretRotation#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#id SecretsmanagerSecretRotation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#tags SecretsmanagerSecretRotation#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(rotation_rules, dict):
            rotation_rules = SecretsmanagerSecretRotationRotationRules(**rotation_rules)
        self._values: typing.Dict[str, typing.Any] = {
            "rotation_lambda_arn": rotation_lambda_arn,
            "rotation_rules": rotation_rules,
            "secret_id": secret_id,
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
    def rotation_lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#rotation_lambda_arn SecretsmanagerSecretRotation#rotation_lambda_arn}.'''
        result = self._values.get("rotation_lambda_arn")
        assert result is not None, "Required property 'rotation_lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rotation_rules(self) -> "SecretsmanagerSecretRotationRotationRules":
        '''rotation_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#rotation_rules SecretsmanagerSecretRotation#rotation_rules}
        '''
        result = self._values.get("rotation_rules")
        assert result is not None, "Required property 'rotation_rules' is missing"
        return typing.cast("SecretsmanagerSecretRotationRotationRules", result)

    @builtins.property
    def secret_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#secret_id SecretsmanagerSecretRotation#secret_id}.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#id SecretsmanagerSecretRotation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#tags SecretsmanagerSecretRotation#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsmanagerSecretRotationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretRotationRotationRules",
    jsii_struct_bases=[],
    name_mapping={"automatically_after_days": "automaticallyAfterDays"},
)
class SecretsmanagerSecretRotationRotationRules:
    def __init__(self, *, automatically_after_days: jsii.Number) -> None:
        '''
        :param automatically_after_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#automatically_after_days SecretsmanagerSecretRotation#automatically_after_days}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "automatically_after_days": automatically_after_days,
        }

    @builtins.property
    def automatically_after_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_rotation#automatically_after_days SecretsmanagerSecretRotation#automatically_after_days}.'''
        result = self._values.get("automatically_after_days")
        assert result is not None, "Required property 'automatically_after_days' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsmanagerSecretRotationRotationRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretsmanagerSecretRotationRotationRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretRotationRotationRulesOutputReference",
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
    @jsii.member(jsii_name="automaticallyAfterDaysInput")
    def automatically_after_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automaticallyAfterDaysInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automaticallyAfterDays")
    def automatically_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automaticallyAfterDays"))

    @automatically_after_days.setter
    def automatically_after_days(self, value: jsii.Number) -> None:
        jsii.set(self, "automaticallyAfterDays", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SecretsmanagerSecretRotationRotationRules]:
        return typing.cast(typing.Optional[SecretsmanagerSecretRotationRotationRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecretsmanagerSecretRotationRotationRules],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretRotationRules",
    jsii_struct_bases=[],
    name_mapping={"automatically_after_days": "automaticallyAfterDays"},
)
class SecretsmanagerSecretRotationRules:
    def __init__(self, *, automatically_after_days: jsii.Number) -> None:
        '''
        :param automatically_after_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#automatically_after_days SecretsmanagerSecret#automatically_after_days}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "automatically_after_days": automatically_after_days,
        }

    @builtins.property
    def automatically_after_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret#automatically_after_days SecretsmanagerSecret#automatically_after_days}.'''
        result = self._values.get("automatically_after_days")
        assert result is not None, "Required property 'automatically_after_days' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsmanagerSecretRotationRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretsmanagerSecretRotationRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretRotationRulesOutputReference",
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
    @jsii.member(jsii_name="automaticallyAfterDaysInput")
    def automatically_after_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automaticallyAfterDaysInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automaticallyAfterDays")
    def automatically_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automaticallyAfterDays"))

    @automatically_after_days.setter
    def automatically_after_days(self, value: jsii.Number) -> None:
        jsii.set(self, "automaticallyAfterDays", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SecretsmanagerSecretRotationRules]:
        return typing.cast(typing.Optional[SecretsmanagerSecretRotationRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecretsmanagerSecretRotationRules],
    ) -> None:
        jsii.set(self, "internalValue", value)


class SecretsmanagerSecretVersion(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretVersion",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version aws_secretsmanager_secret_version}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        secret_binary: typing.Optional[builtins.str] = None,
        secret_string: typing.Optional[builtins.str] = None,
        version_stages: typing.Optional[typing.Sequence[builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version aws_secretsmanager_secret_version} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_id SecretsmanagerSecretVersion#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#id SecretsmanagerSecretVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param secret_binary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_binary SecretsmanagerSecretVersion#secret_binary}.
        :param secret_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_string SecretsmanagerSecretVersion#secret_string}.
        :param version_stages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#version_stages SecretsmanagerSecretVersion#version_stages}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = SecretsmanagerSecretVersionConfig(
            secret_id=secret_id,
            id=id,
            secret_binary=secret_binary,
            secret_string=secret_string,
            version_stages=version_stages,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecretBinary")
    def reset_secret_binary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretBinary", []))

    @jsii.member(jsii_name="resetSecretString")
    def reset_secret_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretString", []))

    @jsii.member(jsii_name="resetVersionStages")
    def reset_version_stages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionStages", []))

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
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretBinaryInput")
    def secret_binary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretBinaryInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretStringInput")
    def secret_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretStringInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionStagesInput")
    def version_stages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "versionStagesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretBinary")
    def secret_binary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretBinary"))

    @secret_binary.setter
    def secret_binary(self, value: builtins.str) -> None:
        jsii.set(self, "secretBinary", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        jsii.set(self, "secretId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretString")
    def secret_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretString"))

    @secret_string.setter
    def secret_string(self, value: builtins.str) -> None:
        jsii.set(self, "secretString", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionStages")
    def version_stages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "versionStages"))

    @version_stages.setter
    def version_stages(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "versionStages", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.secretsmanager.SecretsmanagerSecretVersionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "secret_id": "secretId",
        "id": "id",
        "secret_binary": "secretBinary",
        "secret_string": "secretString",
        "version_stages": "versionStages",
    },
)
class SecretsmanagerSecretVersionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        secret_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        secret_binary: typing.Optional[builtins.str] = None,
        secret_string: typing.Optional[builtins.str] = None,
        version_stages: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''AWS Secrets Manager.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_id SecretsmanagerSecretVersion#secret_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#id SecretsmanagerSecretVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param secret_binary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_binary SecretsmanagerSecretVersion#secret_binary}.
        :param secret_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_string SecretsmanagerSecretVersion#secret_string}.
        :param version_stages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#version_stages SecretsmanagerSecretVersion#version_stages}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "secret_id": secret_id,
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
        if secret_binary is not None:
            self._values["secret_binary"] = secret_binary
        if secret_string is not None:
            self._values["secret_string"] = secret_string
        if version_stages is not None:
            self._values["version_stages"] = version_stages

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
    def secret_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_id SecretsmanagerSecretVersion#secret_id}.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#id SecretsmanagerSecretVersion#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_binary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_binary SecretsmanagerSecretVersion#secret_binary}.'''
        result = self._values.get("secret_binary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#secret_string SecretsmanagerSecretVersion#secret_string}.'''
        result = self._values.get("secret_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_stages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version#version_stages SecretsmanagerSecretVersion#version_stages}.'''
        result = self._values.get("version_stages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsmanagerSecretVersionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAwsSecretsmanagerRandomPassword",
    "DataAwsSecretsmanagerRandomPasswordConfig",
    "DataAwsSecretsmanagerSecret",
    "DataAwsSecretsmanagerSecretConfig",
    "DataAwsSecretsmanagerSecretRotation",
    "DataAwsSecretsmanagerSecretRotationConfig",
    "DataAwsSecretsmanagerSecretRotationRotationRules",
    "DataAwsSecretsmanagerSecretRotationRotationRulesList",
    "DataAwsSecretsmanagerSecretRotationRotationRulesOutputReference",
    "DataAwsSecretsmanagerSecretRotationRules",
    "DataAwsSecretsmanagerSecretRotationRulesList",
    "DataAwsSecretsmanagerSecretRotationRulesOutputReference",
    "DataAwsSecretsmanagerSecretVersion",
    "DataAwsSecretsmanagerSecretVersionConfig",
    "DataAwsSecretsmanagerSecrets",
    "DataAwsSecretsmanagerSecretsConfig",
    "DataAwsSecretsmanagerSecretsFilter",
    "DataAwsSecretsmanagerSecretsFilterList",
    "DataAwsSecretsmanagerSecretsFilterOutputReference",
    "SecretsmanagerSecret",
    "SecretsmanagerSecretConfig",
    "SecretsmanagerSecretPolicy",
    "SecretsmanagerSecretPolicyConfig",
    "SecretsmanagerSecretReplica",
    "SecretsmanagerSecretReplicaList",
    "SecretsmanagerSecretReplicaOutputReference",
    "SecretsmanagerSecretRotation",
    "SecretsmanagerSecretRotationConfig",
    "SecretsmanagerSecretRotationRotationRules",
    "SecretsmanagerSecretRotationRotationRulesOutputReference",
    "SecretsmanagerSecretRotationRules",
    "SecretsmanagerSecretRotationRulesOutputReference",
    "SecretsmanagerSecretVersion",
    "SecretsmanagerSecretVersionConfig",
]

publication.publish()
