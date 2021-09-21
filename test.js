function isQualified() {
  var deferred = new Deferred();

  when(function () {
    return typeof dataLayer != "undefined" && cookies.get("ORA_FPC") != null;
  }).done(() => {
    var campaignTariff = "fix";
    var tariffName = "";
    var smartEligible = "";
    for (var obj of dataLayer) {
      if ("EnergyProduct" in obj) {
        tariffName = obj.EnergyProduct;
      }
      if ("SmartEligible" in obj) {
        smartEligible = obj.SmartEligible;
      }
    }
    if (
      tariffName.toLowerCase().includes(campaignTariff) &&
      smartEligible === "True"
    ) {
      var infinityCookie = cookies.get("ORA_FPC");
      var infinityId = "" + infinityCookie.split(":")[0].split("=")[1];
      visitor.storeId(1, infinityId);
      deferred.resolve();
    } else {
      deferred.reject();
    }
  });

  return deferred;
}

campaign.scope.qualificationRules = campaign.scope.qualificationRules || [];
campaign.scope.qualificationRules.push(isQualified);
