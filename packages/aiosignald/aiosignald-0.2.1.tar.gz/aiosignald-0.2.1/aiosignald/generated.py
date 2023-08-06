"""
Generated using https://signald.org/protocol.json
Version: '0.20.0-7-7d9179fd'
"""

from dataclasses import dataclass, field
import typing as typing_  # avoid conflict with the typing method

from aiosignald.util import JSONProtocol, nested_dataclass, locals_to_request


@dataclass
class Stringv1:
    uri: str
    session_id: str


@dataclass
class JsonMessageRequestResponseMessagev1:
    groupId: str
    person: "JsonAddressv1"
    type: str


@dataclass
class JsonMessageRequestResponseMessagev0:
    groupId: str
    person: "JsonAddressv0"
    type: str


@dataclass
class GroupRequestingMemberv1:
    timestamp: int
    uuid: str


@nested_dataclass
class JsonAccountListv0:
    accounts: typing_.List["JsonAccountv0"] = field(default_factory=list)


@nested_dataclass
class JsonMessageEnvelopev0:
    username: str = None
    uuid: str = None
    source: "JsonAddressv0" = None
    sourceDevice: int = None
    type: str = None
    relay: str = None
    timestamp: int = None
    timestampISO: str = None
    serverTimestamp: int = None
    serverDeliveredTimestamp: int = None
    hasLegacyMessage: bool = None
    hasContent: bool = None
    isUnidentifiedSender: bool = None
    dataMessage: "JsonDataMessagev0" = None
    syncMessage: "JsonSyncMessagev0" = None
    callMessage: "JsonCallMessagev0" = None
    receipt: "JsonReceiptMessagev0" = None
    typing: "JsonTypingMessagev0" = None


@nested_dataclass
class JsonAccountv0:
    deviceId: int = None
    username: str = None
    filename: str = None
    uuid: str = None
    registered: bool = None
    has_keys: bool = None
    subscribed: bool = None


@nested_dataclass
class JsonAddressv0:
    number: str = None
    uuid: str = None
    relay: str = None


@nested_dataclass
class JsonDataMessagev0:
    timestamp: int = None
    attachments: typing_.List["JsonAttachmentv0"] = field(default_factory=list)
    body: str = None
    group: "JsonGroupInfov0" = None
    groupV2: "JsonGroupV2Infov0" = None
    endSession: bool = None
    expiresInSeconds: int = None
    profileKeyUpdate: bool = None
    quote: "JsonQuotev0" = None
    contacts: typing_.List["SharedContactv0"] = field(default_factory=list)
    previews: typing_.List["JsonPreviewv0"] = field(default_factory=list)
    sticker: "JsonStickerv0" = None
    viewOnce: bool = None
    reaction: "JsonReactionv0" = None
    remoteDelete: "RemoteDeletev0" = None
    mentions: typing_.List["JsonMentionv0"] = field(default_factory=list)


@nested_dataclass
class JsonSyncMessagev0:
    sent: "JsonSentTranscriptMessagev0" = None
    contacts: "JsonAttachmentv0" = None
    contactsComplete: bool = None
    groups: "JsonAttachmentv0" = None
    blockedList: "JsonBlockedListMessagev0" = None
    request: str = None
    readMessages: typing_.List["JsonReadMessagev0"] = field(default_factory=list)
    viewOnceOpen: "JsonViewOnceOpenMessagev0" = None
    verified: "JsonVerifiedMessagev0" = None
    configuration: "ConfigurationMessagev0" = None
    stickerPackOperations: typing_.List["JsonStickerPackOperationMessagev0"] = field(
        default_factory=list
    )
    fetchType: str = None
    messageRequestResponse: "JsonMessageRequestResponseMessagev0" = None


@nested_dataclass
class JsonCallMessagev0:
    offerMessage: "OfferMessagev0" = None
    answerMessage: "AnswerMessagev0" = None
    busyMessage: "BusyMessagev0" = None
    hangupMessage: "HangupMessagev0" = None
    iceUpdateMessages: typing_.List["IceUpdateMessagev0"] = field(default_factory=list)
    destinationDeviceId: int = None
    isMultiRing: bool = None


@nested_dataclass
class JsonReceiptMessagev0:
    type: str = None
    timestamps: typing_.List[int] = field(default_factory=list)
    when: int = None


@nested_dataclass
class JsonTypingMessagev0:
    action: str = None
    timestamp: int = None
    groupId: str = None


@nested_dataclass
class JsonAttachmentv0:
    contentType: str = None
    id: str = None
    size: int = None
    storedFilename: str = None
    filename: str = None
    customFilename: str = None
    caption: str = None
    width: int = None
    height: int = None
    voiceNote: bool = None
    key: str = None
    digest: str = None
    blurhash: str = None


@nested_dataclass
class JsonGroupInfov0:
    groupId: str = None
    members: typing_.List["JsonAddressv0"] = field(default_factory=list)
    name: str = None
    type: str = None
    avatarId: int = None


@nested_dataclass
class JsonGroupV2Infov0:
    id: str = None
    revision: int = None
    title: str = None
    description: str = None
    avatar: str = None
    timer: int = None
    members: typing_.List["JsonAddressv0"] = field(default_factory=list)
    pendingMembers: typing_.List["JsonAddressv0"] = field(default_factory=list)
    requestingMembers: typing_.List["JsonAddressv0"] = field(default_factory=list)
    inviteLink: str = None
    accessControl: "GroupAccessControlv0" = None
    memberDetail: typing_.List["GroupMemberv0"] = field(default_factory=list)
    pendingMemberDetail: typing_.List["GroupMemberv0"] = field(default_factory=list)


@nested_dataclass
class JsonQuotev0:
    """
    A quote is a reply to a previous message. ID is the sent time of the message being replied to
    """

    id: int = None
    author: "JsonAddressv0" = None
    text: str = None
    attachments: typing_.List["JsonQuotedAttachmentv0"] = field(default_factory=list)
    mentions: typing_.List["JsonMentionv0"] = field(default_factory=list)


@nested_dataclass
class SharedContactv0:
    name: "Namev0" = None
    avatar: "Optionalv0" = None
    phone: "Optionalv0" = None
    email: "Optionalv0" = None
    address: "Optionalv0" = None
    organization: "Optionalv0" = None


@nested_dataclass
class JsonPreviewv0:
    url: str = None
    title: str = None
    attachment: "JsonAttachmentv0" = None


@nested_dataclass
class JsonStickerv0:
    packID: str = None
    packKey: str = None
    stickerID: int = None
    attachment: "JsonAttachmentv0" = None
    image: str = None


@nested_dataclass
class JsonReactionv0:
    emoji: str = None
    remove: bool = None
    targetAuthor: "JsonAddressv0" = None
    targetSentTimestamp: int = None


@nested_dataclass
class RemoteDeletev0:
    targetSentTimestamp: int = None


@nested_dataclass
class JsonMentionv0:
    uuid: str = None
    start: int = None
    length: int = None


@nested_dataclass
class JsonSentTranscriptMessagev0:
    destination: "JsonAddressv0" = None
    timestamp: int = None
    expirationStartTimestamp: int = None
    message: "JsonDataMessagev0" = None
    unidentifiedStatus: dict = None
    isRecipientUpdate: bool = None


@nested_dataclass
class JsonBlockedListMessagev0:
    addresses: typing_.List["JsonAddressv0"] = field(default_factory=list)
    groupIds: typing_.List[str] = field(default_factory=list)


@nested_dataclass
class JsonReadMessagev0:
    sender: "JsonAddressv0" = None
    timestamp: int = None


@nested_dataclass
class JsonViewOnceOpenMessagev0:
    sender: "JsonAddressv0" = None
    timestamp: int = None


@nested_dataclass
class JsonVerifiedMessagev0:
    destination: "JsonAddressv0" = None
    identityKey: str = None
    verified: str = None
    timestamp: int = None


@nested_dataclass
class ConfigurationMessagev0:
    readReceipts: "Optionalv0" = None
    unidentifiedDeliveryIndicators: "Optionalv0" = None
    typingIndicators: "Optionalv0" = None
    linkPreviews: "Optionalv0" = None


@nested_dataclass
class JsonStickerPackOperationMessagev0:
    packID: str = None
    packKey: str = None
    type: str = None


@nested_dataclass
class OfferMessagev0:
    id: int = None
    sdp: str = None
    type: "Typev0" = None
    opaque: str = None


@nested_dataclass
class AnswerMessagev0:
    id: int = None
    sdp: str = None
    opaque: str = None


@nested_dataclass
class BusyMessagev0:
    id: int = None


@nested_dataclass
class HangupMessagev0:
    id: int = None
    type: "Typev0" = None
    deviceId: int = None
    legacy: bool = None


@nested_dataclass
class IceUpdateMessagev0:
    id: int = None
    opaque: str = None
    sdp: str = None


@nested_dataclass
class JsonQuotedAttachmentv0:
    contentType: str = None
    fileName: str = None
    thumbnail: "JsonAttachmentv0" = None


@nested_dataclass
class GroupAccessControlv0:
    """
    group access control settings. Options for each controlled action are: UNKNOWN, ANY, MEMBER, ADMINISTRATOR, UNSATISFIABLE and UNRECOGNIZED
    """

    link: str = None
    attributes: str = None
    members: str = None


@nested_dataclass
class GroupMemberv0:
    uuid: str = None
    role: str = None
    joined_revision: int = None


@nested_dataclass
class Namev0:
    display: "Optionalv0" = None
    given: "Optionalv0" = None
    family: "Optionalv0" = None
    prefix: "Optionalv0" = None
    suffix: "Optionalv0" = None
    middle: "Optionalv0" = None


@nested_dataclass
class Optionalv0:
    empty: bool = None
    present: bool = None


@nested_dataclass
class Typev0:
    pass


@nested_dataclass
class ClientMessageWrapperv1:
    """
    Wraps all incoming messages sent to the client after a v1 subscribe request is issued
    """

    type: str = None
    version: str = None
    data: dict = None
    error: bool = None
    account: str = None


@nested_dataclass
class IncomingMessagev1:
    account: str = None
    source: "JsonAddressv1" = None
    type: str = None
    timestamp: int = None
    source_device: int = None
    server_receiver_timestamp: int = None
    server_deliver_timestamp: int = None
    has_legacy_message: bool = None
    has_content: bool = None
    unidentified_sender: bool = None
    data_message: "JsonDataMessagev1" = None
    sync_message: "JsonSyncMessagev1" = None
    call_message: "CallMessagev1" = None
    receipt_message: "ReceiptMessagev1" = None
    typing_message: "TypingMessagev1" = None
    story_message: "StoryMessagev1" = None
    server_guid: str = None


@nested_dataclass
class ListenerStatev1:
    """
    prior attempt to indicate signald connectivity state. WebSocketConnectionState messages will be delivered at the  same time as well as in other parts of the websocket lifecycle.
    """

    connected: bool = None


@nested_dataclass
class WebSocketConnectionStatev1:
    """
    indicates when the websocket connection state to the signal server has changed
    """

    state: str = None
    socket: str = None


@nested_dataclass
class StorageChangev1:
    """
    Broadcast to subscribed clients when there is a state change from the storage service
    """

    version: int = None


@nested_dataclass
class SendResponsev1:
    results: typing_.List["JsonSendMessageResultv1"] = field(default_factory=list)
    timestamp: int = None


@nested_dataclass
class JsonVersionMessagev1:
    name: str = None
    version: str = None
    branch: str = None
    commit: str = None


@nested_dataclass
class JsonGroupV2Infov1:
    """
    Information about a Signal group
    """

    id: str = None
    revision: int = None
    title: str = None
    description: str = None
    avatar: str = None
    timer: int = None
    members: typing_.List["JsonAddressv1"] = field(default_factory=list)
    pendingMembers: typing_.List["JsonAddressv1"] = field(default_factory=list)
    requestingMembers: typing_.List["JsonAddressv1"] = field(default_factory=list)
    inviteLink: str = None
    accessControl: "GroupAccessControlv1" = None
    memberDetail: typing_.List["GroupMemberv1"] = field(default_factory=list)
    pendingMemberDetail: typing_.List["GroupMemberv1"] = field(default_factory=list)
    announcements: str = None
    removed: bool = None
    banned_members: typing_.List["BannedGroupMemberv1"] = field(default_factory=list)
    group_change: "GroupChangev1" = None


@nested_dataclass
class LinkedDevicesv1:
    devices: typing_.List["DeviceInfov1"] = field(default_factory=list)


@nested_dataclass
class JsonGroupJoinInfov1:
    groupID: str = None
    title: str = None
    description: str = None
    memberCount: int = None
    addFromInviteLink: int = None
    revision: int = None
    pendingAdminApproval: bool = None


@nested_dataclass
class GroupInfov1:
    """
    A generic type that is used when the group version is not known
    """

    v1: "JsonGroupInfov1" = None
    v2: "JsonGroupV2Infov1" = None


@nested_dataclass
class SetProfilev1:
    account: str = None
    name: str = None
    avatarFile: str = None
    about: str = None
    emoji: str = None
    mobilecoin_address: str = None
    visible_badge_ids: typing_.List[str] = field(default_factory=list)


@nested_dataclass
class JsonAddressv1:
    number: str = None
    uuid: str = None
    relay: str = None


@nested_dataclass
class Profilev1:
    """
    Information about a Signal user
    """

    name: str = None
    avatar: str = None
    address: "JsonAddressv1" = None
    capabilities: "Capabilitiesv1" = None
    color: str = None
    about: str = None
    emoji: str = None
    contact_name: str = None
    profile_name: str = None
    inbox_position: int = None
    expiration_time: int = None
    mobilecoin_address: str = None
    visible_badge_ids: typing_.List[str] = field(default_factory=list)


@nested_dataclass
class GroupListv1:
    groups: typing_.List["JsonGroupV2Infov1"] = field(default_factory=list)
    legacyGroups: typing_.List["JsonGroupInfov1"] = field(default_factory=list)


@nested_dataclass
class ProfileListv1:
    profiles: typing_.List["Profilev1"] = field(default_factory=list)


@nested_dataclass
class LinkingURIv1:
    uri: str = None
    session_id: str = None


@nested_dataclass
class Accountv1:
    """
    A local account in signald
    """

    address: "JsonAddressv1" = None
    pending: bool = None
    pni: str = None
    device_id: int = None
    account_id: str = None


@nested_dataclass
class IdentityKeyListv1:
    """
    a list of identity keys associated with a particular address
    """

    address: "JsonAddressv1" = None
    identities: typing_.List["IdentityKeyv1"] = field(default_factory=list)


@nested_dataclass
class AccountListv1:
    accounts: typing_.List["Accountv1"] = field(default_factory=list)


@nested_dataclass
class GetAllIdentitiesv1:
    """
    get all known identity keys
    """

    account: str = None


@nested_dataclass
class AllIdentityKeyListv1:
    identity_keys: typing_.List["IdentityKeyListv1"] = field(default_factory=list)


@nested_dataclass
class ServerListv1:
    servers: typing_.List["Serverv1"] = field(default_factory=list)


@nested_dataclass
class RemoteConfigListv1:
    config: typing_.List["RemoteConfigv1"] = field(default_factory=list)


@nested_dataclass
class BooleanMessagev1:
    """
    A message containing a single boolean, usually as a response
    """

    value: bool = None


@nested_dataclass
class GroupHistoryPagev1:
    """
    The result of fetching a group's history along with paging data.
    """

    results: typing_.List["GroupHistoryEntryv1"] = field(default_factory=list)
    paging_data: "PagingDatav1" = None


@nested_dataclass
class JsonSendMessageResultv1:
    address: "JsonAddressv1" = None
    success: "SendSuccessv1" = None
    networkFailure: bool = None
    unregisteredFailure: bool = None
    identityFailure: str = None
    proof_required_failure: "ProofRequiredErrorv1" = None


@nested_dataclass
class IdentityKeyv1:
    added: int = None
    safety_number: str = None
    qr_code_data: str = None
    trust_level: str = None


@nested_dataclass
class JsonDataMessagev1:
    timestamp: int = None
    attachments: typing_.List["JsonAttachmentv1"] = field(default_factory=list)
    body: str = None
    group: "JsonGroupInfov1" = None
    groupV2: "JsonGroupV2Infov1" = None
    endSession: bool = None
    expiresInSeconds: int = None
    profileKeyUpdate: bool = None
    quote: "JsonQuotev1" = None
    contacts: typing_.List["SharedContactv1"] = field(default_factory=list)
    previews: typing_.List["JsonPreviewv1"] = field(default_factory=list)
    sticker: "JsonStickerv0" = None
    viewOnce: bool = None
    reaction: "JsonReactionv1" = None
    remoteDelete: "RemoteDeletev1" = None
    mentions: typing_.List["JsonMentionv1"] = field(default_factory=list)
    payment: "Paymentv1" = None
    is_expiration_update: bool = None
    group_call_update: str = None
    story_context: "StoryContextv1" = None


@nested_dataclass
class JsonSyncMessagev1:
    sent: "JsonSentTranscriptMessagev1" = None
    contacts: "JsonAttachmentv1" = None
    contactsComplete: bool = None
    groups: "JsonAttachmentv1" = None
    blockedList: "JsonBlockedListMessagev1" = None
    request: str = None
    readMessages: typing_.List["JsonReadMessagev1"] = field(default_factory=list)
    viewOnceOpen: "JsonViewOnceOpenMessagev1" = None
    verified: "JsonVerifiedMessagev1" = None
    configuration: "ConfigurationMessagev0" = None
    stickerPackOperations: typing_.List["JsonStickerPackOperationMessagev0"] = field(
        default_factory=list
    )
    fetchType: str = None
    messageRequestResponse: "JsonMessageRequestResponseMessagev1" = None


@nested_dataclass
class CallMessagev1:
    offer_message: "OfferMessagev1" = None
    answer_message: "AnswerMessagev1" = None
    busy_message: "BusyMessagev1" = None
    hangup_message: "HangupMessagev1" = None
    ice_update_message: typing_.List["IceUpdateMessagev1"] = field(default_factory=list)
    destination_device_id: int = None
    multi_ring: bool = None


@nested_dataclass
class ReceiptMessagev1:
    type: str = None
    timestamps: typing_.List[int] = field(default_factory=list)
    when: int = None


@nested_dataclass
class TypingMessagev1:
    action: str = None
    timestamp: int = None
    group_id: str = None


@nested_dataclass
class StoryMessagev1:
    group: "JsonGroupV2Infov1" = None
    file: "JsonAttachmentv1" = None
    text: "TextAttachmentv1" = None
    allow_replies: bool = None


@nested_dataclass
class JsonAttachmentv1:
    """
    represents a file attached to a message. When sending, only `filename` is required.
    """

    contentType: str = None
    id: str = None
    size: int = None
    storedFilename: str = None
    filename: str = None
    customFilename: str = None
    caption: str = None
    width: int = None
    height: int = None
    voiceNote: bool = None
    key: str = None
    digest: str = None
    blurhash: str = None


@nested_dataclass
class JsonQuotev1:
    """
    A quote is a reply to a previous message. ID is the sent time of the message being replied to
    """

    id: int = None
    author: "JsonAddressv1" = None
    text: str = None
    attachments: typing_.List["JsonQuotedAttachmentv0"] = field(default_factory=list)
    mentions: typing_.List["JsonMentionv1"] = field(default_factory=list)


@nested_dataclass
class JsonMentionv1:
    uuid: str = None
    start: int = None
    length: int = None


@nested_dataclass
class JsonPreviewv1:
    """
    metadata about one of the links in a message
    """

    url: str = None
    title: str = None
    description: str = None
    date: int = None
    attachment: "JsonAttachmentv1" = None


@nested_dataclass
class JsonReactionv1:
    emoji: str = None
    remove: bool = None
    targetAuthor: "JsonAddressv1" = None
    targetSentTimestamp: int = None


@nested_dataclass
class GroupAccessControlv1:
    """
    group access control settings. Options for each controlled action are: UNKNOWN, ANY, MEMBER, ADMINISTRATOR, UNSATISFIABLE and UNRECOGNIZED
    """

    link: str = None
    attributes: str = None
    members: str = None


@nested_dataclass
class GroupMemberv1:
    uuid: str = None
    role: str = None
    joined_revision: int = None


@nested_dataclass
class BannedGroupMemberv1:
    uuid: str = None
    timestamp: int = None


@nested_dataclass
class GroupChangev1:
    """
    Represents a group change made by a user. This can also represent request link invites. Only the fields relevant to the group change performed will be set. Note that in signald, group changes are currently only received from incoming messages from a message subscription.
    """

    editor: "JsonAddressv1" = None
    revision: int = None
    new_members: typing_.List["GroupMemberv1"] = field(default_factory=list)
    delete_members: typing_.List["JsonAddressv1"] = field(default_factory=list)
    modify_member_roles: typing_.List["GroupMemberv1"] = field(default_factory=list)
    modified_profile_keys: typing_.List["GroupMemberv1"] = field(default_factory=list)
    new_pending_members: typing_.List["GroupPendingMemberv1"] = field(
        default_factory=list
    )
    delete_pending_members: typing_.List["JsonAddressv1"] = field(default_factory=list)
    promote_pending_members: typing_.List["GroupMemberv1"] = field(default_factory=list)
    new_banned_members: typing_.List["BannedGroupMemberv1"] = field(
        default_factory=list
    )
    new_unbanned_members: typing_.List["BannedGroupMemberv1"] = field(
        default_factory=list
    )
    new_title: str = None
    new_avatar: bool = None
    new_timer: int = None
    new_access_control: "GroupAccessControlv1" = None
    new_requesting_members: typing_.List["GroupRequestingMemberv1"] = field(
        default_factory=list
    )
    delete_requesting_members: typing_.List["JsonAddressv1"] = field(
        default_factory=list
    )
    promote_requesting_members: typing_.List["GroupMemberv1"] = field(
        default_factory=list
    )
    new_invite_link_password: bool = None
    new_description: str = None
    new_is_announcement_group: str = None


@nested_dataclass
class DeviceInfov1:
    id: int = None
    name: str = None
    created: int = None
    lastSeen: int = None


@nested_dataclass
class JsonGroupInfov1:
    """
    information about a legacy group
    """

    groupId: str = None
    members: typing_.List["JsonAddressv1"] = field(default_factory=list)
    name: str = None
    type: str = None
    avatarId: int = None


@nested_dataclass
class Capabilitiesv1:
    gv2: bool = None
    storage: bool = None
    stories: bool = None
    gv1_migration: bool = None
    sender_key: bool = None
    announcement_group: bool = None
    change_number: bool = None


@nested_dataclass
class Serverv1:
    """
    a Signal server
    """

    uuid: str = None
    proxy: str = None
    ca: str = None
    service_url: str = None
    cdn_urls: typing_.List["ServerCDNv1"] = field(default_factory=list)
    contact_discovery_url: str = None
    key_backup_url: str = None
    storage_url: str = None
    zk_param: str = None
    unidentified_sender_root: str = None
    key_backup_service_name: str = None
    key_backup_service_id: str = None
    key_backup_mrenclave: str = None
    cds_mrenclave: str = None
    ias_ca: str = None


@nested_dataclass
class Paymentv1:
    """
    details about a MobileCoin payment
    """

    receipt: str = None
    note: str = None


@nested_dataclass
class RemoteConfigv1:
    """
    A remote config (feature flag) entry.
    """

    name: str = None
    value: str = None


@nested_dataclass
class GroupHistoryEntryv1:
    group: "JsonGroupV2Infov1" = None
    change: "GroupChangev1" = None


@nested_dataclass
class PagingDatav1:
    has_more_pages: bool = None
    next_page_revision: int = None


@nested_dataclass
class JsonViewOnceOpenMessagev1:
    sender: "JsonAddressv1" = None
    timestamp: int = None


@nested_dataclass
class SendSuccessv1:
    unidentified: bool = None
    needsSync: bool = None
    duration: int = None
    devices: typing_.List[int] = field(default_factory=list)


@nested_dataclass
class SharedContactv1:
    name: "SharedContactNamev1" = None
    email: typing_.List["SharedContactEmailv1"] = field(default_factory=list)
    phone: typing_.List["SharedContactPhonev1"] = field(default_factory=list)
    address: typing_.List["SharedContactAddressv1"] = field(default_factory=list)
    avatar: "SharedContactAvatarv1" = None
    organization: str = None


@nested_dataclass
class RemoteDeletev1:
    target_sent_timestamp: int = None


@nested_dataclass
class StoryContextv1:
    author: str = None
    sent_timestamp: int = None


@nested_dataclass
class JsonSentTranscriptMessagev1:
    destination: "JsonAddressv1" = None
    timestamp: int = None
    expirationStartTimestamp: int = None
    message: "JsonDataMessagev1" = None
    story: "StoryMessagev1" = None
    unidentifiedStatus: dict = None
    isRecipientUpdate: bool = None


@nested_dataclass
class JsonBlockedListMessagev1:
    addresses: typing_.List["JsonAddressv1"] = field(default_factory=list)
    groupIds: typing_.List[str] = field(default_factory=list)


@nested_dataclass
class JsonReadMessagev1:
    sender: "JsonAddressv1" = None
    timestamp: int = None


@nested_dataclass
class JsonVerifiedMessagev1:
    destination: "JsonAddressv1" = None
    identityKey: str = None
    verified: str = None
    timestamp: int = None


@nested_dataclass
class OfferMessagev1:
    id: int = None
    sdp: str = None
    type: str = None
    opaque: str = None


@nested_dataclass
class AnswerMessagev1:
    id: int = None
    sdp: str = None
    opaque: str = None


@nested_dataclass
class BusyMessagev1:
    id: int = None


@nested_dataclass
class HangupMessagev1:
    id: int = None
    type: str = None
    legacy: bool = None
    device_id: int = None


@nested_dataclass
class IceUpdateMessagev1:
    id: int = None
    opaque: str = None
    sdp: str = None


@nested_dataclass
class TextAttachmentv1:
    text: str = None
    style: str = None
    preview: "JsonPreviewv1" = None
    text_foreground_color: str = None
    text_background_color: str = None
    background_gradient: "Gradientv1" = None
    background_color: str = None


@nested_dataclass
class GroupPendingMemberv1:
    uuid: str = None
    role: str = None
    timestamp: int = None
    added_by_uuid: str = None


@nested_dataclass
class ServerCDNv1:
    number: int = None
    url: str = None


@nested_dataclass
class SharedContactNamev1:
    display: str = None
    given: str = None
    middle: str = None
    family: str = None
    prefix: str = None
    suffix: str = None


@nested_dataclass
class SharedContactEmailv1:
    type: str = None
    value: str = None
    label: str = None


@nested_dataclass
class SharedContactPhonev1:
    type: str = None
    value: str = None
    label: str = None


@nested_dataclass
class SharedContactAddressv1:
    type: str = None
    label: str = None
    street: str = None
    pobox: str = None
    neighborhood: str = None
    city: str = None
    region: str = None
    postcode: str = None
    country: str = None


@nested_dataclass
class SharedContactAvatarv1:
    attachment: "JsonAttachmentv1" = None
    is_profile: bool = None


@nested_dataclass
class Gradientv1:
    start_color: str = None
    end_color: str = None


class SignaldGeneratedAPI(JSONProtocol):
    async def send(
        self,
        username: str = None,
        account: str = None,
        recipientAddress: "JsonAddressv1" = None,
        recipientGroupId: str = None,
        messageBody: str = None,
        attachments: typing_.List["JsonAttachmentv1"] = None,
        quote: "JsonQuotev1" = None,
        timestamp: int = None,
        mentions: typing_.List["JsonMentionv1"] = None,
        previews: typing_.List["JsonPreviewv1"] = None,
        members: typing_.List["JsonAddressv1"] = None,
    ) -> SendResponsev1:
        """


        :param username: Example: "+12024561414"
        :param account: Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param recipientAddress:
        :param recipientGroupId: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param messageBody: Example: "hello"
        :param attachments:
        :param quote:
        :param timestamp:
        :param mentions:
        :param previews:
        :param members: Optionally set to a sub-set of group members. Ignored if recipientGroupId isn't specified
        """

        return SendResponsev1(
            **await self.get_response(
                {"type": "send", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def react(
        self,
        username: str = None,
        recipientAddress: "JsonAddressv1" = None,
        recipientGroupId: str = None,
        reaction: "JsonReactionv1" = None,
        timestamp: int = None,
        members: typing_.List["JsonAddressv1"] = None,
    ) -> SendResponsev1:
        """
        react to a previous message

        :param username: Example: "+12024561414"
        :param recipientAddress:
        :param recipientGroupId: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param reaction:
        :param timestamp:
        :param members: Optionally set to a sub-set of group members. Ignored if recipientGroupId isn't specified
        """

        return SendResponsev1(
            **await self.get_response(
                {"type": "react", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def version(
        self,
    ) -> JsonVersionMessagev1:
        """ """

        return JsonVersionMessagev1(
            **await self.get_response(
                {"type": "version", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def accept_invitation(
        self,
        account: str = None,
        groupID: str = None,
    ) -> JsonGroupV2Infov1:
        """
        Accept a v2 group invitation. Note that you must have a profile name set to join groups.

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param groupID: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {
                    "type": "accept_invitation",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def approve_membership(
        self,
        account: str = None,
        groupID: str = None,
        members: typing_.List["JsonAddressv1"] = None,
    ) -> JsonGroupV2Infov1:
        """
        approve a request to join a group

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param groupID: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param members: list of requesting members to approve
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {
                    "type": "approve_membership",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def get_group(
        self,
        account: str = None,
        groupID: str = None,
        revision: int = None,
    ) -> JsonGroupV2Infov1:
        """
        Query the server for the latest state of a known group. If the account is not a member of the group, an UnknownGroupError is returned.

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param groupID: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param revision: the latest known revision, default value (-1) forces fetch from server
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {"type": "get_group", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def get_linked_devices(
        self,
        account: str = None,
    ) -> LinkedDevicesv1:
        """
        list all linked devices on a Signal account

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        """

        return LinkedDevicesv1(
            **await self.get_response(
                {
                    "type": "get_linked_devices",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def join_group(
        self,
        account: str = None,
        uri: str = None,
    ) -> JsonGroupJoinInfov1:
        """
        Join a group using the a signal.group URL. Note that you must have a profile name set to join groups.

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param uri: The signal.group URL Example: "https://signal.group/#CjQKINH_GZhXhfifTcnBkaKTNRxW-hHKnGSq-cJNyPVqHRp8EhDUB7zjKNEl0NaULhsqJCX3"
        """

        return JsonGroupJoinInfov1(
            **await self.get_response(
                {"type": "join_group", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def remove_linked_device(
        self,
        account: str = None,
        deviceId: int = None,
    ):
        """
        Remove a linked device from the Signal account. Only allowed when the local device id is 1

        :param account: The account to interact with Example: "+12024561414"
        :param deviceId: the ID of the device to unlink Example: 3
        """

        await self.get_response(
            {
                "type": "remove_linked_device",
                "version": "v1",
                **locals_to_request(locals()),
            }
        )

    async def update_group(
        self,
        account: str = None,
        groupID: str = None,
        title: str = None,
        description: str = None,
        avatar: str = None,
        updateTimer: int = None,
        addMembers: typing_.List["JsonAddressv1"] = None,
        removeMembers: typing_.List["JsonAddressv1"] = None,
        updateRole: "GroupMemberv1" = None,
        updateAccessControl: "GroupAccessControlv1" = None,
        resetLink: bool = None,
        announcements: str = None,
    ) -> GroupInfov1:
        """
        modify a group. Note that only one modification action may be performed at once

        :param account: The identifier of the account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param groupID: the ID of the group to update Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param title: Example: "Parkdale Run Club"
        :param description: A new group description. Set to empty string to remove an existing description. Example: "A club for running in Parkdale"
        :param avatar: Example: "/tmp/image.jpg"
        :param updateTimer: update the group timer.
        :param addMembers:
        :param removeMembers:
        :param updateRole:
        :param updateAccessControl: note that only one of the access controls may be updated per request
        :param resetLink: regenerate the group link password, invalidating the old one
        :param announcements: ENABLED to only allow admins to post messages, DISABLED to allow anyone to post
        """

        return GroupInfov1(
            **await self.get_response(
                {"type": "update_group", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def set_profile(
        self,
        account: str = None,
        name: str = None,
        avatarFile: str = None,
        about: str = None,
        emoji: str = None,
        mobilecoin_address: str = None,
        visible_badge_ids: typing_.List[str] = None,
    ):
        """


        :param account: The phone number of the account to use Example: "+12024561414"
        :param name: Change the profile name Example: "signald user"
        :param avatarFile: Path to new profile avatar file. If unset or null, unset the profile avatar Example: "/tmp/image.jpg"
        :param about: Change the 'about' profile field
        :param emoji: Change the profile emoji
        :param mobilecoin_address: Change the profile payment address. Payment address must be a *base64-encoded* MobileCoin address. Note that this is not the traditional MobileCoin address encoding, which is custom. Clients are responsible for converting between MobileCoin's custom base58 on the user-facing side and base64 encoding on the signald side.
        :param visible_badge_ids: configure visible badge IDs
        """

        await self.get_response(
            {"type": "set_profile", "version": "v1", **locals_to_request(locals())}
        )

    async def resolve_address(
        self,
        account: str = None,
        partial: "JsonAddressv1" = None,
    ) -> JsonAddressv1:
        """
        Resolve a partial JsonAddress with only a number or UUID to one with both. Anywhere that signald accepts a JsonAddress will except a partial, this is a convenience function for client authors, mostly because signald doesn't resolve all the partials it returns.

        :param account: The signal account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param partial: The partial address, missing fields
        """

        return JsonAddressv1(
            **await self.get_response(
                {
                    "type": "resolve_address",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def mark_read(
        self,
        account: str = None,
        to: "JsonAddressv1" = None,
        timestamps: typing_.List[int] = None,
        when: int = None,
    ):
        """


        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param to: The address that sent the message being marked as read
        :param timestamps: List of messages to mark as read Example: 1615576442475
        :param when:
        """

        await self.get_response(
            {"type": "mark_read", "version": "v1", **locals_to_request(locals())}
        )

    async def get_profile(
        self,
        account: str = None,
        async_: bool = None,
        address: "JsonAddressv1" = None,
    ) -> Profilev1:
        """
        Get all information available about a user

        :param account: the signald account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param async_: if true, return results from local store immediately, refreshing from server in the background if needed. if false (default), block until profile can be retrieved from server
        :param address: the address to look up
        """

        return Profilev1(
            **await self.get_response(
                {"type": "get_profile", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def list_groups(
        self,
        account: str = None,
    ) -> GroupListv1:
        """


        :param account: Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        """

        return GroupListv1(
            **await self.get_response(
                {"type": "list_groups", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def list_contacts(
        self,
        account: str = None,
        async_: bool = None,
    ) -> ProfileListv1:
        """


        :param account: Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param async_: return results from local store immediately, refreshing from server afterward if needed. If false (default), block until all pending profiles have been retrieved.
        """

        return ProfileListv1(
            **await self.get_response(
                {
                    "type": "list_contacts",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def create_group(
        self,
        account: str = None,
        title: str = None,
        avatar: str = None,
        members: typing_.List["JsonAddressv1"] = None,
        timer: int = None,
        member_role: str = None,
    ) -> JsonGroupV2Infov1:
        """


        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param title: Example: "Parkdale Run Club"
        :param avatar: Example: "/tmp/image.jpg"
        :param members:
        :param timer: the message expiration timer
        :param member_role: The role of all members other than the group creator. Options are ADMINISTRATOR or DEFAULT (case insensitive) Example: "ADMINISTRATOR"
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {"type": "create_group", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def leave_group(
        self,
        account: str = None,
        groupID: str = None,
    ) -> GroupInfov1:
        """


        :param account: The account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param groupID: The group to leave Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        """

        return GroupInfov1(
            **await self.get_response(
                {"type": "leave_group", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def generate_linking_uri(
        self,
        server: str = None,
    ) -> LinkingURIv1:
        """
        Generate a linking URI. Typically this is QR encoded and scanned by the primary device. Submit the returned session_id with a finish_link request.

        :param server: The identifier of the server to use. Leave blank for default (usually Signal production servers but configurable at build time)
        """

        return LinkingURIv1(
            **await self.get_response(
                {
                    "type": "generate_linking_uri",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def finish_link(
        self,
        overwrite: bool = None,
        device_name: str = None,
        session_id: str = None,
    ) -> Accountv1:
        """
        After a linking URI has been requested, finish_link must be called with the session_id provided with the URI. it will return information about the new account once the linking process is completed by the other device and the new account is setup. Note that the account setup process can sometimes take some time, if rapid userfeedback is required after scanning, use wait_for_scan first, then finish setup with finish_link.

        :param overwrite: overwrite existing account data if the phone number conflicts. false by default
        :param device_name:
        :param session_id:
        """

        return Accountv1(
            **await self.get_response(
                {"type": "finish_link", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def add_device(
        self,
        account: str = None,
        uri: str = None,
    ):
        """
        Link a new device to a local Signal account

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param uri: the sgnl://linkdevice uri provided (typically in qr code form) by the new device Example: "sgnl://linkdevice?uuid=jAaZ5lxLfh7zVw5WELd6-Q&pub_key=BfFbjSwmAgpVJBXUdfmSgf61eX3a%2Bq9AoxAVpl1HUap9"
        """

        await self.get_response(
            {"type": "add_device", "version": "v1", **locals_to_request(locals())}
        )

    async def register(
        self,
        account: str = None,
        voice: bool = None,
        captcha: str = None,
        server: str = None,
    ) -> Accountv1:
        """
        begin the account registration process by requesting a phone number verification code. when the code is received, submit it with a verify request

        :param account: the e164 phone number to register with Example: "+12024561414"
        :param voice: set to true to request a voice call instead of an SMS for verification
        :param captcha: See https://signald.org/articles/captcha/
        :param server: The identifier of the server to use. Leave blank for default (usually Signal production servers but configurable at build time)
        """

        return Accountv1(
            **await self.get_response(
                {"type": "register", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def verify(
        self,
        account: str = None,
        code: str = None,
    ) -> Accountv1:
        """
        verify an account's phone number with a code after registering, completing the account creation process

        :param account: the e164 phone number being verified Example: "+12024561414"
        :param code: the verification code, dash (-) optional Example: "555555"
        """

        return Accountv1(
            **await self.get_response(
                {"type": "verify", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def get_identities(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
    ) -> IdentityKeyListv1:
        """
        Get information about a known keys for a particular address

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address: address to get keys for
        """

        return IdentityKeyListv1(
            **await self.get_response(
                {
                    "type": "get_identities",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def trust(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        safety_number: str = None,
        qr_code_data: str = None,
        trust_level: str = None,
    ):
        """
        Trust another user's safety number using either the QR code data or the safety number text

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address: The user to query identity keys for
        :param safety_number: required if qr_code_data is absent Example: "373453558586758076680580548714989751943247272727416091564451"
        :param qr_code_data: base64-encoded QR code data. required if safety_number is absent
        :param trust_level: One of TRUSTED_UNVERIFIED, TRUSTED_VERIFIED or UNTRUSTED. Default is TRUSTED_VERIFIED Example: "TRUSTED_VERIFIED"
        """

        await self.get_response(
            {"type": "trust", "version": "v1", **locals_to_request(locals())}
        )

    async def delete_account(
        self,
        account: str = None,
        server: bool = None,
    ):
        """
        delete all account data signald has on disk, and optionally delete the account from the server as well. Note that this is not "unlink" and will delete the entire account, even from a linked device.

        :param account: The account to delete Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param server: delete account information from the server as well (default false)
        """

        await self.get_response(
            {"type": "delete_account", "version": "v1", **locals_to_request(locals())}
        )

    async def typing(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        group: str = None,
        typing: bool = None,
        when: int = None,
    ):
        """
        send a typing started or stopped message

        :param account: The account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address:
        :param group: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param typing: Example: true
        :param when:
        """

        await self.get_response(
            {"type": "typing", "version": "v1", **locals_to_request(locals())}
        )

    async def reset_session(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        timestamp: int = None,
    ) -> SendResponsev1:
        """
        reset a session with a particular user

        :param account: The account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address: the user to reset session with
        :param timestamp:
        """

        return SendResponsev1(
            **await self.get_response(
                {
                    "type": "reset_session",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def request_sync(
        self,
        groups: bool = None,
        configuration: bool = None,
        contacts: bool = None,
        blocked: bool = None,
        keys: bool = None,
        account: str = None,
    ):
        """
        Request other devices on the account send us their group list, syncable config and contact list.

        :param groups: request group sync (default true)
        :param configuration: request configuration sync (default true)
        :param contacts: request contact sync (default true)
        :param blocked: request block list sync (default true)
        :param keys: request storage service keys
        :param account: The account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        """

        await self.get_response(
            {"type": "request_sync", "version": "v1", **locals_to_request(locals())}
        )

    async def list_accounts(
        self,
    ) -> AccountListv1:
        """
        return all local accounts

        """

        return AccountListv1(
            **await self.get_response(
                {
                    "type": "list_accounts",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def group_link_info(
        self,
        account: str = None,
        uri: str = None,
    ) -> JsonGroupJoinInfov1:
        """
        Get information about a group from a signal.group link

        :param account: The account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param uri: the signald.group link Example: "https://signal.group/#CjQKINH_GZhXhfifTcnBkaKTNRxW-hHKnGSq-cJNyPVqHRp8EhDUB7zjKNEl0NaULhsqJCX3"
        """

        return JsonGroupJoinInfov1(
            **await self.get_response(
                {
                    "type": "group_link_info",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def update_contact(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        name: str = None,
        color: str = None,
        inbox_position: int = None,
    ) -> Profilev1:
        """
        update information about a local contact

        :param account: Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address:
        :param name:
        :param color:
        :param inbox_position:
        """

        return Profilev1(
            **await self.get_response(
                {
                    "type": "update_contact",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def set_expiration(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        group: str = None,
        expiration: int = None,
    ) -> SendResponsev1:
        """
        Set the message expiration timer for a thread. Expiration must be specified in seconds, set to 0 to disable timer

        :param account: The account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address:
        :param group: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param expiration: Example: 604800
        """

        return SendResponsev1(
            **await self.get_response(
                {
                    "type": "set_expiration",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def set_device_name(
        self,
        account: str = None,
        device_name: str = None,
    ):
        """
        set this device's name. This will show up on the mobile device on the same account under settings -> linked devices

        :param account: The account to set the device name of Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param device_name: The device name
        """

        await self.get_response(
            {"type": "set_device_name", "version": "v1", **locals_to_request(locals())}
        )

    async def get_all_identities(
        self,
        account: str = None,
    ) -> AllIdentityKeyListv1:
        """
        get all known identity keys

        :param account: The account to interact with Example: "+12024561414"
        """

        return AllIdentityKeyListv1(
            **await self.get_response(
                {
                    "type": "get_all_identities",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def subscribe(
        self,
        account: str = None,
    ):
        """
        receive incoming messages. After making a subscribe request, incoming messages will be sent to the client encoded as ClientMessageWrapper. Send an unsubscribe request or disconnect from the socket to stop receiving messages.

        :param account: The account to subscribe to incoming message for Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        """

        await self.get_response(
            {"type": "subscribe", "version": "v1", **locals_to_request(locals())}
        )

    async def unsubscribe(
        self,
        account: str = None,
    ):
        """
        See subscribe for more info

        :param account: The account to unsubscribe from Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        """

        await self.get_response(
            {"type": "unsubscribe", "version": "v1", **locals_to_request(locals())}
        )

    async def remote_delete(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        group: str = None,
        timestamp: int = None,
        members: typing_.List["JsonAddressv1"] = None,
    ) -> SendResponsev1:
        """
        delete a message previously sent

        :param account: the account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address: the address to send the delete message to. should match address the message to be deleted was sent to. required if group is not set.
        :param group: the group to send the delete message to. should match group the message to be deleted was sent to. required if address is not set. Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param timestamp:
        :param members: Optionally set to a sub-set of group members. Ignored if group isn't specified
        """

        return SendResponsev1(
            **await self.get_response(
                {
                    "type": "remote_delete",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def add_server(
        self,
        server: "Serverv1" = None,
    ) -> Stringv1:
        """
        add a new server to connect to. Returns the new server's UUID.

        :param server:
        """

        return Stringv1(
            **await self.get_response(
                {"type": "add_server", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def get_servers(
        self,
    ) -> ServerListv1:
        """ """

        return ServerListv1(
            **await self.get_response(
                {"type": "get_servers", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def delete_server(
        self,
        uuid: str = None,
    ):
        """


        :param uuid:
        """

        await self.get_response(
            {"type": "delete_server", "version": "v1", **locals_to_request(locals())}
        )

    async def send_payment(
        self,
        account: str = None,
        address: "JsonAddressv1" = None,
        payment: "Paymentv1" = None,
        when: int = None,
    ) -> SendResponsev1:
        """
        send a mobilecoin payment

        :param account: the account to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param address: the address to send the payment message to
        :param payment:
        :param when:
        """

        return SendResponsev1(
            **await self.get_response(
                {"type": "send_payment", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def get_remote_config(
        self,
        account: str = None,
    ) -> RemoteConfigListv1:
        """
        Retrieves the remote config (feature flags) from the server.

        :param account: The account to use to retrieve the remote config Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        """

        return RemoteConfigListv1(
            **await self.get_response(
                {
                    "type": "get_remote_config",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def refuse_membership(
        self,
        account: str = None,
        members: typing_.List["JsonAddressv1"] = None,
        group_id: str = None,
        also_ban: bool = None,
    ) -> JsonGroupV2Infov1:
        """
        deny a request to join a group

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param members: list of requesting members to refuse
        :param group_id: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param also_ban:
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {
                    "type": "refuse_membership",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def submit_challenge(
        self,
        account: str = None,
        challenge: str = None,
        captcha_token: str = None,
    ):
        """


        :param account: Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param challenge:
        :param captcha_token:
        """

        await self.get_response(
            {"type": "submit_challenge", "version": "v1", **locals_to_request(locals())}
        )

    async def is_identifier_registered(
        self,
        account: str = None,
        identifier: str = None,
    ) -> BooleanMessagev1:
        """
        Determine whether an account identifier is registered on the Signal service.

        :param account: The account to use to use Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param identifier: The UUID of an identifier to check if it is registered on Signal. This UUID is either a Phone Number Identity (PNI) or an Account Identity (ACI). Example: "aeed01f0-a234-478e-8cf7-261c283151e7"
        """

        return BooleanMessagev1(
            **await self.get_response(
                {
                    "type": "is_identifier_registered",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def wait_for_scan(
        self,
        session_id: str = None,
    ):
        """
        An optional part of the linking process. Intended to be called after displaying the QR code, will return quickly after the user scans the QR code. finish_link must be called after wait_for_scan returns a non-error

        :param session_id:
        """

        await self.get_response(
            {"type": "wait_for_scan", "version": "v1", **locals_to_request(locals())}
        )

    async def get_group_revision_pages(
        self,
        account: str = None,
        group_id: str = None,
        from_revision: int = None,
        include_first_revision: bool = None,
    ) -> GroupHistoryPagev1:
        """
        Query the server for group revision history. The history contains information about the changes between each revision and the user that made the change.

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param group_id: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param from_revision: The revision to start the pages from. Note that if this is lower than the revision you joined the group, an AuthorizationFailedError is returned.
        :param include_first_revision: Whether to include the first state in the returned pages (default false)
        """

        return GroupHistoryPagev1(
            **await self.get_response(
                {
                    "type": "get_group_revision_pages",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def send_sync_message(
        self,
        account: str = None,
        view_once_open_message: "JsonViewOnceOpenMessagev1" = None,
        message_request_response: "JsonMessageRequestResponseMessagev1" = None,
    ) -> JsonSendMessageResultv1:
        """
        Sends a sync message to the account's devices

        :param account: Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param view_once_open_message: This can be set to indicate to other devices about having viewed a view-once message.
        :param message_request_response: This can be set to indicate to other devices about a response to an incoming message request from an unknown user or group. Warning: Using the BLOCK and BLOCK_AND_DELETE options relies on other devices to do the blocking, and it does not make you leave the group!
        """

        return JsonSendMessageResultv1(
            **await self.get_response(
                {
                    "type": "send_sync_message",
                    "version": "v1",
                    **locals_to_request(locals()),
                }
            )
        )

    async def ban_user(
        self,
        account: str = None,
        group_id: str = None,
        users: typing_.List["JsonAddressv1"] = None,
    ) -> JsonGroupV2Infov1:
        """
        Bans users from a group. This works even if the users aren't in the group. If they are currently in the group, they will also be removed.

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param group_id: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param users: List of users to ban
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {"type": "ban_user", "version": "v1", **locals_to_request(locals())}
            )
        )

    async def unban_user(
        self,
        account: str = None,
        group_id: str = None,
        users: typing_.List["JsonAddressv1"] = None,
    ) -> JsonGroupV2Infov1:
        """
        Unbans users from a group.

        :param account: The account to interact with Example: "0cc10e61-d64c-4dbc-b51c-334f7dd45a4a"
        :param group_id: Example: "EdSqI90cS0UomDpgUXOlCoObWvQOXlH5G3Z2d3f4ayE="
        :param users: List of users to unban
        """

        return JsonGroupV2Infov1(
            **await self.get_response(
                {"type": "unban_user", "version": "v1", **locals_to_request(locals())}
            )
        )
